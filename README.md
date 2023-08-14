# fhirdemo-project
Make sure you have latest cdk cli
```
npm -g uninstall aws-cdk
npm -g install aws-cdk
```
**Ensure you have python version 3 running**
```
python -V
```
**Create venv**
```
python -m venv
python -m pip install aws-cdk-lib
python -m pip install --upgrade pip
source ./bin/activate
```
**Verify cdk is okay**
```
cdk synth
```
**Deploy Workshop infrastructure using cdk deploy**
```
cdk deploy FhirdemoProjectStack --parameters ahldatastore="https://healthlake.us-east-1.amazonaws.com/datastore/16a9465c648e06a74cc29eb276619d86/r4/" -—parameters secretname="fhir/demo/secret" -—parameters regionname="us-east-1" -—parameters vpccidr="172.31.100.0/24" —-parameters subnetsize=26
```
**Once the cloudformation stack is complete, get the instance id from the Cloudformation output; Go to EC2 console; SSH Connect from EC2 console**
Once you are in the shell console run the following.
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




