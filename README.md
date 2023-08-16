# fhirdemo-project

Git clone
```
mkdir fhir
cd fhir
git clone https://github.com/raghavendraprakash/fhirdemo-project.git
cd fhirdemo-project
```
**Simple way using CFT console.**
Upload CFT file (<root_folder>/ehrdb_to_fhir_ahl.yaml) <br>
Input the values for the parameters: <br>
ahldatastore=https://healthlake.us-east-1.amazonaws.com/datastore/16a9465c648e06a74cc29eb276619d86/r4/ <br>
secretname=fhir/demo/secret <br>
regionname=us-east-1 <br>
vpccidr=172.31.100.0/24 <br>
subnetsize=26 <br>

**----------------------------------------- OPTIONAL BEGIN -------------------------------------------** <br>
**[Optional] If you want to use CDK and develop further, use Cloud9 IDE*** <br>
**Ensure you have python version 3 running; Python3.7 will also work**  <br>
```
python -V
```
**Create venv**
```
python -m pip install --upgrade pip
python -m venv venv
source venv/bin/activate
python -m pip install aws-cdk-lib
```
**Verify cdk is okay**
```
cdk synth
```
**Deploy Workshop infrastructure using cdk deploy**

![image](https://github.com/raghavendraprakash/fhirdemo-project/assets/6112970/ca230938-2ae6-42c7-ae95-629557df86ad)


```
cdk deploy FhirdemoProjectStack --parameters ahldatastore="https://healthlake.us-east-1.amazonaws.com/datastore/16a9465c648e06a74cc29eb276619d86/r4/" -—parameters secretname="fhir/demo/secret" -—parameters regionname="us-east-1" -—parameters vpccidr="172.31.100.0/24" —-parameters subnetsize=26
```
**----------------------------------------- OPTIONAL END -------------------------------------------** <br>
<br> 

<br>

**Once the cloudformation stack is complete, get the instance id from the Cloudformation output; Go to EC2 console; SSH Connect from EC2 console**
<Br> Once you are in the shell console run the following.

![image](https://github.com/raghavendraprakash/fhirdemo-project/assets/6112970/f5a78ade-68fa-4fd4-8ae6-8ece9840384a)

1/ Create ehrdatamodel.sql [Copy the content from ehrdatamodel.sql from the git project and save] <Project_root>/ehrsampledata/ehrdatamodel.sql
```
vi ehrdatamodel.sql
```
2/ Create TestDataGenerator.java; Copy the content from <Project_root>/ehrsampledata/TestDataGenerator.java and save it.
```
vi TestDataGenerator.java
```
3/ Compile TestDataGenerator.java
```
javac TestDataGenerator.java
```
4/ Run TestDataGenerator
```
java TestDataGenerator
```
Ensure ehrsampledata.sql file is generated in the current directory.

**Connect to RDS host and create tables and insert the sample data**
From the cloudformation stack output, note down the RDS host.
From the AWS Console, Go to secrets manager, retrieve the secret value stored for the secret name fhir/demo/secret; Note down the password.<br>
Modify the parameter values appropriately in the below command while connecting to RDS host.
```
psql --host=<rds_host> --username=postgres --password
```
Execute the following (Ensure the semicolon ends the command)
```
\i ehrdatamodel.sql;
\i ehrsampledata.sql;
commit;
```
Verify the tables created
```
\dt+;
````
Verify the data is inserted
```
SELECT * FROM PATIENT;
```
You should see sample data inserted.
<br>
**Execute the Lambda (Fetch the data from RDS Host, convert to FHIR resource, post to Amazon HealthLake using FHIR API)**
Go to AWS Lambda console<br>
Click on Test; Create sample test event (dummy event) <br>
Click Test. Your Lambda should execute for about 3 minutes<br>
This Lambda fetches the data from database, converts into FHIR resources, and stores in Amazon HealthLake.<br>
After the successful execution, go to CloudWatch logs, pick any FHIR resource id of patient and Run query against Amazon HealthLake using Amazon HealthLake console's Run query option <br>

**Call to Action**
<br>
1/ Map Practitioner data from RDS table with FHIR resource for Practitioner <br>
2/ Map Encounter data from RDS table with FHIR resource for Encounter; Analyze how can extensions be added to FHIR resources <br>
3/ Think about how can one add extensions to existing FHIR resource, say Patient and update the existing FHIR resource with Practitioner details <br>

Note: Lambda is chosen just to demonstrate the ability to transform table data into FHIR resource; For bulk transfer, make use of bulk import option of FHIR. Employ Lambda as required if there is need for real time capture of the details.
<br>




