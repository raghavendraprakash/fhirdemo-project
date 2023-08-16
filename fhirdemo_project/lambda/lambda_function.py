import boto3
import json
import requests
from requests_auth_aws_sigv4 import AWSSigV4
import sys
import logging
import os
import time
import psycopg2
from botocore.exceptions import ClientError
from dataclasses import dataclass
from psycopg2.extras import RealDictCursor
from fhir.resources.patient import Patient
from fhir.resources.identifier import Identifier
from fhir.resources.patient import PatientCommunication
from fhir.resources.humanname import HumanName
from fhir.resources.fhirreference import FHIRReference
from fhir.resources.fhirdate import FHIRDate
from fhir.resources.valueset import ValueSet
from fhir.resources.coding import Coding
from fhir.resources.organization import Organization
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.address import Address
from datetime import datetime


secret_name = os.environ['SECRET_NAME']
region_name = os.environ['REGION_NAME']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
    get_secret_value_response=get_secret(secret_name, region_name)
    secret_string=json.loads(get_secret_value_response['SecretString'])
    # Decrypts secret using the associated KMS key.
    db_name = secret_string['db_name']
    user_name = secret_string['user_name']
    rds_host = secret_string['rds_host']
    password = secret_string['password']
    datastore_endpoint = secret_string['ahl_datastore']
    
    conn = psycopg2.connect(host = rds_host,  database = db_name,  user = user_name,   password = password )

    
    # TODO implement
    # Set the input arguments
    data_store_endpoint = datastore_endpoint

    #requestBody = {"resourceType": "Patient", "active": True, "name": [{"use": "official","family": "Dow","given": ["Jen444"]},{"use": "usual","given": ["Jen"]}],"gender": "female","birthDate": "1966-09-01"}
    region = region_name
    
    # creating FHIR Patient resource
    #Frame the resource endpoint
    
    session = boto3.session.Session(region_name=region)
    client = session.client("healthlake")
     
    # Frame authorization
    auth = AWSSigV4("healthlake", session=session)    
    
    # Calling data store FHIR endpoint using SigV4 auth
    # Organization - select * from facility f, location l where f.location_id=l.id;
    cur = conn.cursor(cursor_factory = RealDictCursor)
    cur.execute("select * from patient p, facility f where p.registered_at=f.id limit 3;")
    resource_path = "Patient"
    resource_endpoint = data_store_endpoint+resource_path
    for record in cur:
        recordAsStr=json.dumps(record, default=str)
        requestBody=createFhirPatient(recordAsStr)
        r = requests.post(resource_endpoint, json=requestBody, auth=auth)
        print(r.json())  
        time.sleep(2)

    
    cur = conn.cursor(cursor_factory = RealDictCursor)
    cur.execute("select * from facility f, location l where f.location_id=l.id;")
    resource_path="Organization"
    resource_endpoint = data_store_endpoint+resource_path
    for record in cur:
        recordAsStr=json.dumps(record, default=str)
        requestBody=createFhirOrg(recordAsStr)
        r = requests.post(resource_endpoint, json=requestBody, auth=auth)
        print(r.json())  
        time.sleep(2)

    conn.close()
    
    return requestBody
    
def get_secret(secret_name, region_name):
    secret_name = secret_name
    region_name = region_name
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e
    return get_secret_value_response

    
def createFhirOrg(recordAsStr):
    record=json.loads(recordAsStr)
    org = Organization()
    org.id = record["id"]
    org.type=list()
    codeableconcept=CodeableConcept()
    codeableconcept.text=record["type"]
    org.type.append(codeableconcept)
    org.active = True
    org.name = record["name"]
    org.address = list()
    address = Address()
    address.type="both"
    address.postalCode=record["post_code"]
    address.line=list()
    address.line.append(record["addressline_1"])
    address.line.append(record["addressline_2"])
    address.line.append("lattitude "+record["lattitude"])
    address.line.append("longitude "+record["longitude"])
    address.city=record["city"]
    address.country = record["country"]
    org.address.append(address)
    return org.as_json()

def createFhirPatient(recordAsStr):
    record=json.loads(recordAsStr)
    patient = Patient()
    patient.id=record["id"]
    patient.identifier=list()

    iden=Identifier()
    idType=CodeableConcept()
    idType.text="SystemId"
    iden.type=idType
    iden.value=record["id"]
    patient.identifier.append(iden)
    
    iden=Identifier()
    idType=CodeableConcept()
    idType.text="ABHA_NUMBER"
    iden.type=idType
    iden.value=record["abha_number"]
    patient.identifier.append(iden)    
    
    iden=Identifier()
    idType=CodeableConcept()
    idType.text="MRN"
    iden.type=idType
    iden.value=record["mrn"]
    patient.identifier.append(iden)


    iden=Identifier()
    idType=CodeableConcept()
    idType.text="DL_NUMBER"
    iden.type=idType
    iden.value=record["dl_number"]
    patient.identifier.append(iden)
    
    iden=Identifier()
    idType=CodeableConcept()
    idType.text="PASSPORT_NUMBER"
    iden.type=idType
    iden.value=record["passport_number"]
    patient.identifier.append(iden) 

    patient.active=True
    patient.name=list()
    humanName=HumanName()
    humanName.use="usual"
    humanName.text=record["name"]
    patient.name.append(humanName)
    patient.gender=record["gender"]
    patient.deceasedBoolean=False
    maritalStatusCC=CodeableConcept()
    maritalStatusCC.coding=list()
    mCoding=Coding()
    if "Y"==record["ismarried"]:
        mCoding.display="Married"
        mCoding.code="M"
    maritalStatusCC.coding.append(mCoding)
    maritalStatusCC.text=record["ismarried"]
    patient.maritalStatus=maritalStatusCC
    patient.multipleBirthBoolean=False
    patient.communication=list()
    codeableconcept=CodeableConcept()
    codeableconcept.text=record["language"]
    codeableconcept.code="en"    
    patientCommunication=PatientCommunication()
    patientCommunication.language=codeableconcept
    patientCommunication.preferred=True
    patient.communication.append(patientCommunication)
    ref=FHIRReference()
    ref.reference=record["registered_at"]
    ref.display="Reference to Organization"
    patient.managingOrganization=ref
    datetime_str = record["birth_date"]
    datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d').date()
    fhirDate = FHIRDate()
    fhirDate.date=datetime_object
    print(type(datetime_object))
    print(datetime_object)
    patient.birthDate=fhirDate
    return patient.as_json()
