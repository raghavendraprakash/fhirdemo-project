from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    CfnOutput,
    CfnParameter,
    RemovalPolicy,
    SecretValue,
    aws_secretsmanager as secretsmanager,
    aws_lambda as _lambda,   
    aws_iam as iam,
    aws_rds as rds,
    aws_ec2 as ec2
)
import json

# VPC CIDR that will be used to create a new VPC (default)
VPC_CIDR =  "172.31.200.0/24"
# Subnet size of the subnets in the Local Zone (default)
SUBNET_SIZE = 26

class FhirdemoProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        ahl_datastore = CfnParameter(self, "ahldatastore").value_as_string
        secret_name =  CfnParameter(self, "secretname").value_as_string
        region_name =  CfnParameter(self, "regionname").value_as_string
        
        VPC_CIDR = CfnParameter(self, "vpccidr").value_as_string
        SUBNET_SIZE = CfnParameter(self, "subnetsize", type="Number").value_as_number
        
        env=json.loads("{}")
        env["SECRET_NAME"]=secret_name
        env["REGION_NAME"]=region_name

        #create DB, store credentials in Secrets Manager
        
        fhirVpc=self.create_VPC()

        # Templated secret with username and password fields
        templated_secret = secretsmanager.Secret(self, "TemplatedSecret",
            generate_secret_string=secretsmanager.SecretStringGenerator(
                secret_string_template=json.dumps({"username": "postgres"}),
                generate_string_key="password",
                exclude_characters='/@}{][%#)(-+^*=_\&"'
            )
        )        

        #create SG for RDS and one for Lambda
        fhirLambda_sg = ec2.SecurityGroup(self, "FHIRLambda-SecurityGroup",
            vpc=fhirVpc,
            description="Allow outbound access ...",
            allow_all_outbound=True,
            disable_inline_rules=True
        )
        fhirLambda_sg.add_ingress_rule(ec2.Peer.ipv4("0.0.0.0/0"), ec2.Port.tcp(22), "allow ssh traffic from the 0.0.0.0/0")
        fhirLambda_sg.add_ingress_rule(fhirLambda_sg, ec2.Port.all_traffic(), "allow traffic from the same security group")
        #Sequence of fhirLambda_sg
        fhirLambda_sgs=[fhirLambda_sg]

        rds_sg = ec2.SecurityGroup(self, "RDS-SecurityGroup",
            vpc=fhirVpc,
            description="Allow ssh access to ec2 instances",
            allow_all_outbound=True,
            disable_inline_rules=True
        )
        
        rds_sg.add_ingress_rule(fhirLambda_sg, ec2.Port.all_traffic(), "allow traffic from the same FHIR Lambda security group")
        rds_sg.add_ingress_rule(rds_sg, ec2.Port.all_traffic(), "allow traffic from the same security group")
        #Sequence of rds_sg
        rds_sgs=[rds_sg]
        # Using the templated secret as credentials; default is publicly accessible
        cred=rds.Credentials.from_password("postgres", templated_secret.secret_value_from_json("password"))
        dbInstance = rds.DatabaseInstance(self, "fhirdemodb",
            engine=rds.DatabaseInstanceEngine.POSTGRES,
            credentials=cred,
            security_groups=rds_sgs,
            vpc=fhirVpc
        )
        
        fhirLambda=self.create_Lambda(fhirVpc, env, fhirLambda_sgs)
        
        dbInstanceEndpointAddress = dbInstance.db_instance_endpoint_address
        
        secretsmanager.Secret(
                        self, 
                        "Secret", 
                        secret_name=secret_name,
                        secret_object_value={
                                "ahl_datastore": SecretValue.unsafe_plain_text(ahl_datastore),
                                "user_name": SecretValue.unsafe_plain_text("postgres"),
                                "db_name": SecretValue.unsafe_plain_text("postgres"),
                                "password": templated_secret.secret_value_from_json("password"),
                                "rds_host": SecretValue.unsafe_plain_text(str(dbInstanceEndpointAddress)),
                            }
                         )
        
        instance=self.create_Instance(fhirVpc, fhirLambda_sg)
            
        CfnOutput(self, "AHL Datastore URL ", value=ahl_datastore)
        CfnOutput(self, "EHR DB Host Endpoint ", value=str(dbInstanceEndpointAddress))
        CfnOutput(self, "Connect through console to operate on DB ", value=instance.instance_id)

    def create_VPC(self):
        vpc = ec2.Vpc(
            self,
            "Vpc",
            ip_addresses = ec2.IpAddresses.cidr(VPC_CIDR),
            subnet_configuration = [
                ec2.SubnetConfiguration(
                    name = 'Public-Subnet-',
                    subnet_type = ec2.SubnetType.PUBLIC,
                    cidr_mask = SUBNET_SIZE,
                ),
                ec2.SubnetConfiguration(
                    name = 'Private-Subnet-',
                    subnet_type = ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask = SUBNET_SIZE,
                ),
            ], 
            nat_gateways=1
        )
        return vpc

    def create_Lambda(self, fhirVpc, env, fhirLambda_sgs):
        
        # create Role
        lambda_role = iam.Role(self, "Role",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            description="Lambda Execution role"
        )
        lambda_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaVPCAccessExecutionRole")) 
        lambda_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")) 
        # create Policy
        fhirdemoPolicy = iam.Policy(self, "FHIR-Workshop-Access-Policy",
            statements=[iam.PolicyStatement(
                actions=["ec2:CreateNetworkInterface", "secretsmanager:GetSecretValue", "kms:GenerateDataKey", "healthlake:CreateResource", "ec2:DescribeNetworkInterfaces", "ec2:DeleteNetworkInterface"],
                resources=["*"]
        )])
        fhirdemoPolicy.attach_to_role (lambda_role)     
        
        # create layer
        layerPg = _lambda.LayerVersion(self, 'aws_psycopg_layer',
                                     code=_lambda.Code.from_asset("fhirdemo_project/lambda_layer/awspsycopg"),
                                     description='Common helper utility to connect to postgres db',
                                     compatible_runtimes=[
                                         _lambda.Runtime.PYTHON_3_8
                                     ],
                                     removal_policy=RemovalPolicy.DESTROY
                                     )
        layerSigv4 = _lambda.LayerVersion(self, 'aws_sigv4_layer',
                                     code=_lambda.Code.from_asset("fhirdemo_project/lambda_layer/awssigv4"),
                                     description='Common helper utility for signing requests',
                                     compatible_runtimes=[
                                         _lambda.Runtime.PYTHON_3_8
                                     ],
                                     removal_policy=RemovalPolicy.DESTROY
                                     )                                     
        layerFhirLib = _lambda.LayerVersion(self, 'aws_fhirlib_layer',
                                     code=_lambda.Code.from_asset("fhirdemo_project/lambda_layer/awsfhir4lib"),
                                     description='Common helper utility for creating fhir resources',
                                     compatible_runtimes=[
                                         _lambda.Runtime.PYTHON_3_8
                                     ],
                                     removal_policy=RemovalPolicy.DESTROY
                                     )   
                                     # create lambda function
        fhirLambda = _lambda.Function(self, "lambda_function",
                                    runtime=_lambda.Runtime.PYTHON_3_8,
                                    handler="lambda_function.lambda_handler",
                                    vpc=fhirVpc,
                                    security_groups=fhirLambda_sgs,
                                    environment=env,
                                    timeout=Duration.seconds(180),
                                    code=_lambda.Code.from_asset("fhirdemo_project/lambda"),
                                    role=lambda_role,
                                    layers=[layerPg, layerSigv4, layerFhirLib])
        return fhirLambda
                                    
    def create_Instance(self, fhirVpc, lambda_Sg):
        subnets=json.loads("{}")
        subnets["subnet_type"]=ec2.SubnetType.PUBLIC
        
        userdata=ec2.UserData.for_linux()
        userdata.add_commands("sudo yum update;sudo amazon-linux-extras enable postgresql14;sudo yum install postgresql -y;sudo amazon-linux-extras enable corretto8;sudo yum install java-1.8.0-amazon-corretto-devel -y;")

        instance = ec2.Instance(self, "fhirdbClientInstance",
            vpc=fhirVpc,
            vpc_subnets=subnets,
            security_group=lambda_Sg,
            instance_name="FHIRDBClientInstance",
            user_data=userdata,
            associate_public_ip_address=True,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO),
            machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2)
        )
        return instance
