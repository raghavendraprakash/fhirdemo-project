# fhirdemo-project

Please use Cloud9 IDE. <br>
Clone the code repository
```
mkdir fhir
cd fhir
git clone https://github.com/raghavendraprakash/fhirdemo-project.git
cd fhirdemo-project
```

<br>

**Ensure you have python version 3 running; Python3.7 will also work** 

```
python -V
```
**Create Virtual Environment for Python3**
```
python -m venv .venv
source .venv/bin/activate
python -m pip install aws-cdk-lib
python -m pip install --upgrade pip
```
**Run cdk bootstrap...**
```
cdk bootstrap
```

**Deployment Architecture**
<br><br>
![image](https://github.com/raghavendraprakash/fhirdemo-project/assets/6112970/ca230938-2ae6-42c7-ae95-629557df86ad)
<br>
**Deploy Workshop infrastructure using cdk deploy**
```
cdk deploy FhirdemoProjectStack --parameters ahldatastore="https://healthlake.<REGION_NAME>.amazonaws.com/datastore/<DATASTORE_ID>/r4/" --parameters secretname="fhir/demo/secret" --parameters regionname="<REGION_NAME>" --parameters vpccidr="172.31.100.0/24" --parameters subnetsize=26
```
<br> 

<br>

**Provision Test data model and Test data**
<br><br>
**Data Model**
<br><br>
![image](https://github.com/raghavendraprakash/fhirdemo-project/assets/6112970/f5a78ade-68fa-4fd4-8ae6-8ece9840384a)
<br>
**Once the cloudformation stack is complete, get the instance_id from the Cloudformation output; Go to EC2 console; SSH Connect from EC2 console**
<Br> Once you are in the EC2 SSH shell console run the following.

1/ Create ehrdatamodel.sql [Copy the content from ehrdatamodel.sql from the project structure and save] Locate here ...<Project_root>/ehrsampledata/ehrdatamodel.sql
```
vi ehrdatamodel.sql 
```
esc a > paste content > esc wq <br>
2/ Create TestDataGenerator.java; Copy the content from <Project_root>/ehrsampledata/TestDataGenerator.java and save it.
```
vi TestDataGenerator.java  
```
esc a > paste content > esc wq <br>

3/ Compile TestDataGenerator.java
```
javac TestDataGenerator.java
```
4/ Run TestDataGenerator
```
java TestDataGenerator
```
Ensure ehrsampledata.sql file is generated in the current directory.
<br><br>
**Execute SQL files - Connect to RDS host;Create tables;Insert the sample data**
From the cloudformation stack output, note down the RDS host. <br>
From the AWS Console, Go to secrets manager, retrieve the secret value stored for the secret name fhir/demo/secret (Remember the value you provided during infrastructure provisioning); Note down the password.<br>
Modify the parameter values appropriately in the below command while connecting to RDS host.
```
psql --host=<rds_host> --username=postgres --password
```
Execute the following (Ensure the semicolon ends the command)
```
\c postgres
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
<br><br>

**Fetch data from RDS HOST and store in Amazon HealthLake**
<br><br>
Lambda does the following <br>
- Fetch the data from RDS Host <br>
- Convert to FHIR format <br>
- Post to Amazon HealthLake using FHIR API (Signed requests) <br>
<br>
Go to AWS Lambda console<br>
Click on Test; Create sample test event (dummy event) <br>
Click Test. Your Lambda should execute for about 3 minutes<br>
This Lambda fetches the data from database, converts into FHIR resources, and stores in Amazon HealthLake.<br>
<br>
After the successful execution, go to CloudWatch logs, pick any FHIR resource id of patient and Run query against Amazon HealthLake using Amazon HealthLake console's Run query option <br>
<br><br>

**Call to Action**
<br>
**Sample Mapping**
<br>
![image](https://github.com/raghavendraprakash/fhirdemo-project/assets/6112970/89f7cc0b-cb35-44c6-aee9-7aec7cf492fe)

<br>
1/ Map Practitioner data from RDS table with FHIR resource for Practitioner <br>
2/ Map Encounter data from RDS table with FHIR resource for Encounter; Analyze how can extensions be added to FHIR resources <br>
3/ Think about how can one add extensions to existing FHIR resource, say Patient and update the existing FHIR resource with Practitioner details <br>
<br>
Reference: https://build.fhir.org/patient.html
<br>
Note: Lambda is chosen just to demonstrate the ability to transform table data into FHIR resource; For bulk transfer, make use of bulk import option of FHIR. Employ Lambda as required if there is need for real time capture of the details.
<br>
<br>
**Credits**
<br>
Lambda layer for FHIR Resource libray - https://github.com/nazrulworld/fhir.resources/tree/4.0.0 <br>
[BSD License](https://github.com/nazrulworld/fhir.resources/blob/main/LICENSE) <br>

Lambda layer for connecting to RDS PostgreSQL - https://pypi.org/project/aws-psycopg2/ <br>
[MIT License](https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+MIT+License)




