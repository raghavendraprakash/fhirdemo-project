import java.util.ArrayList;
import java.util.GregorianCalendar;
import java.util.List;
import java.util.Random;
import java.util.UUID;
import java.sql.Timestamp;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.sql.Date;

/**
 * @author praghavs
 * 1/ Create 500 random patient profiles
 * 2/ Create 50 random practitioner profiles
 * 3/ Create 3 Organizations - Hospital, Clinic
 * 4/ Create 10 facilities - Clinics
 * 5/ Create 5 
 *
 */

public class TestDataGenerator {

  public static void main(String[] args) throws Exception {
	  //System.out.print("UUID = " +  UUID.randomUUID().toString());
	  Timestamp now = new Timestamp(System.currentTimeMillis());
	  Date dt = new Date(now.getTime());
	  StringBuffer buffer = new StringBuffer();
	  
	  List<Location> listLocations = new ArrayList<Location>();
	  {
		  Location location = new Location();
		  location.id = UUID.randomUUID().toString();
		  location.name="ChurchStreet Branch";
		  location.addressLine1 = "122, BVK Street";
		  location.addressLine2= "New building, Church Street";
		  location.postCode= "560012";
		  location.city="Bengaluru";
		  location.state="Karnataka";
		  location.country="India";
		  location.lattitude="12.97495";
		  location.longitude="77.60946";
		  location.lastUpdatedTime=now;
		  listLocations.add(location);
		  
		  Location location2 = new Location();
		  location2.id = UUID.randomUUID().toString();
		  location2.name="FLD Heights";
		  location2.addressLine1 = "212, RR Street";
		  location2.addressLine2= "FLD Glucon complex";
		  location2.postCode= "560022";
		  location2.city="Bengaluru";
		  location2.state="Karnataka";
		  location2.country="India";
		  location2.lattitude="12.97495";
		  location2.longitude="77.60946";
		  location2.lastUpdatedTime=now;		  
		  listLocations.add(location2);	

		  Location location3 = new Location();
		  location3.id = UUID.randomUUID().toString();
		  location3.name="Beacon Towers";
		  location3.addressLine1 = "121, MG Road";
		  location3.addressLine2= "Beacon Towers";
		  location3.postCode= "560021";
		  location3.city="Bengaluru";
		  location3.state="Karnataka";
		  location3.country="India";
		  location3.lattitude="12.97495";
		  location3.longitude="77.60946";
		  location3.lastUpdatedTime=now;		  
		  listLocations.add(location3);	
		  
		  Location location4 = new Location();
		  location4.id = UUID.randomUUID().toString();
		  location4.name="DM Crown";
		  location4.addressLine1 = "321, DM Road";
		  location4.addressLine2= "Cleo Dome";
		  location4.postCode= "560101";
		  location4.city="Bengaluru";
		  location4.state="Karnataka";
		  location4.country="India";
		  location4.lattitude="12.97495";
		  location4.longitude="77.60946";
		  location4.lastUpdatedTime=now;		  
		  listLocations.add(location4);	
		  
		  Location location5 = new Location();
		  location5.id = UUID.randomUUID().toString();
		  location5.name="BGYes Apolo";
		  location5.addressLine1 = "321, BGS Road";
		  location5.addressLine2= "Namaste Building";
		  location5.postCode= "560059";
		  location5.city="Bengaluru";
		  location5.state="Karnataka";
		  location5.country="India";
		  location5.lattitude="12.97495";
		  location5.longitude="77.60946";
		  location5.lastUpdatedTime=now;		  
		  listLocations.add(location5);			  
	  }
	  for (Location location : listLocations) {
		  buffer.append(location.getSql()+"\n");
		  System.out.println (location.getSql());
	  }
	  
	  // Facility
	  
	  List<Facility> listFacility = new ArrayList<Facility>();
	  int lcMin=0, lcMax=4;
	  {
		  Facility facility = new Facility();
		  facility.id = UUID.randomUUID().toString();
		  facility.lastUpdatedTime=now;
		  facility.name="Polygon clinic";
		  facility.type="Clinic";
		  facility.locationId=((Location) listLocations.get(getRandom(lcMin, lcMax))).id;
		  listFacility.add(facility);
		  
		  Facility facility2 = new Facility();
		  facility2.id = UUID.randomUUID().toString();
		  facility2.lastUpdatedTime=now;
		  facility2.name="Apolo Hospitals";
		  facility2.type="Hospital";
		  facility2.locationId=((Location) listLocations.get(getRandom(lcMin, lcMax))).id;
		  listFacility.add(facility2);
		  
		  Facility facility3 = new Facility();
		  facility3.id = UUID.randomUUID().toString();
		  facility3.lastUpdatedTime=now;
		  facility3.name="Fortease Network";
		  facility3.type="Hospital";
		  facility3.locationId=((Location) listLocations.get(getRandom(lcMin, lcMax))).id;
		  listFacility.add(facility3);

		  Facility facility4 = new Facility();
		  facility4.id = UUID.randomUUID().toString();
		  facility4.lastUpdatedTime=now;
		  facility4.name="Mannippal Network";
		  facility4.type="Hospital";
		  facility4.locationId=((Location) listLocations.get(getRandom(lcMin, lcMax))).id;
		  listFacility.add(facility4);	
		  
		  Facility facility5 = new Facility();
		  facility5.id = UUID.randomUUID().toString();
		  facility5.lastUpdatedTime=now;
		  facility5.name="Manassa Clnic";
		  facility5.type="Clinic";
		  facility5.locationId=((Location) listLocations.get(getRandom(lcMin, lcMax))).id;
		  listFacility.add(facility5);	
		  
	  }
	  for (Facility facility : listFacility) {
		  buffer.append(facility.getSql()+"\n");
		  System.out.println (facility.getSql());
	  }	  
	  
	  // Patient
	  List<Patient> listPatient = new ArrayList<Patient>();
	  int ptMin=0,ptMax=4;
	  {		  
		  int limit=100;
		  int i=0;
		  while (i<limit) {
			  Patient patient = new Patient();
			  patient.id=UUID.randomUUID().toString();
			  patient.deceasedDate=null;
			  patient.isDeceased="F";
			  patient.dlNumber="DL-"+UUID.randomUUID().toString();
			  patient.abhaNumber="ABHA-"+UUID.randomUUID().toString();
			  patient.passportNumber="PP-"+UUID.randomUUID().toString();
			  patient.mrn="MRN-"+UUID.randomUUID().toString();
			  patient.phoneNumber="+91"+"9388200000";
			  patient.firstName="FirstName-"+i;
			  patient.lastName="LastName-"+i;
			  patient.email=patient.firstName+"@gnail.com";
			  patient.givenName="GivenName-"+i;
			  patient.mothersMaidenName="MothersName-"+i;
			  patient.gender= ((getRandom(0, 1) == 0) ? "M" : "F");
			  patient.sex = patient.gender;
			  patient.isMarried=((getRandom(0, 1) == 0) ? "Y" : "N");
			  patient.disabilityAdjYrs=getRandom(75, 80);
			  patient.qualityAdjYrs=getRandom(65, 70);
			  patient.registeredAt=((Facility)listFacility.get(getRandom(ptMin, ptMax))).id;
			  patient.registeredOn=now;
			  patient.birthDate=new Date (getDateInMillies(getRandom(1970, 1980), getRandom(1, 12), getRandom(1, 31)));
			  patient.language="English";
			  patient.race="Indian";
			  patient.lastUpdatedTime=now;
			  
			  listPatient.add(patient);
			  i++;
		  }
		  for (Patient patient : listPatient) {
			  buffer.append(patient.getSql()+"\n");
			  System.out.println (patient.getSql());
		  }	 		  
	  }
	  
	  
	  // Practitioner
	  String[] specializationArr =  new String[10];
	  specializationArr[0]="Dermatology";
	  specializationArr[1]="Endocrinology";
	  specializationArr[2]="Paediatrics";
	  specializationArr[3]="Orthodontics";
	  specializationArr[4]="Orthopedics";
	  specializationArr[5]="Neurology";
	  specializationArr[6]="ENT";
	  specializationArr[7]="Ophtamology";
	  specializationArr[8]="Psychiatry";
	  specializationArr[8]="Naturopathy";

	  List<Practitioner> listPractitioner = new ArrayList<Practitioner>();
	  int prMin=0,prMax=10;
	  {
		  int limit=10;
		  int i=0;		  
		  while (i<limit) {
			  Practitioner practitioner = new Practitioner();
			  practitioner.id=UUID.randomUUID().toString();
			  practitioner.phoneNumber="+91"+"9511100000";
			  practitioner.firstName="FirstName-"+i;
			  practitioner.lastName="LastName-"+i;
			  practitioner.givenName="GivenName-"+i;
			  practitioner.gender= ((getRandom(0, 1) == 0) ? "M" : "F");
			  practitioner.birthDate=new Date (getDateInMillies(getRandom(1970, 1980), getRandom(1, 12), getRandom(1, 31)));
			  practitioner.aadhaarId="AADHAAR-"+UUID.randomUUID().toString();
			  practitioner.email=practitioner.firstName+"@practition.er";
			  practitioner.language="English";
			  practitioner.organizationId=((Facility)listFacility.get(getRandom(lcMin, lcMax))).id;
			  practitioner.pan="PAN-"+UUID.randomUUID().toString();
			  practitioner.passportNumber="PP-"+UUID.randomUUID().toString();
			  practitioner.primaryLocation=practitioner.organizationId;
			  practitioner.qualification="M.B.B.S, M.D";
			  practitioner.sex=((getRandom(0, 1) == 0) ? "M" : "F");
			  practitioner.specialization=specializationArr[getRandom(0, 9)];
			  practitioner.lastUpdatedTime=now;
			  
			  listPractitioner.add(practitioner);
			  i++;
		  }
		  for (Practitioner practitioner : listPractitioner) {
			  buffer.append(practitioner.getSql()+"\n");
			  System.out.println (practitioner.getSql());
		  }	 		  
	  }
	  
	  // Encounter
	  String[] encounterType =  new String[5];
	  encounterType[0]="GeneralCheckup";
	  encounterType[1]="Surgery";
	  encounterType[2]="RoutineCheckup";
	  encounterType[3]="FollowUp";
	  encounterType[4]="Treatment";
 

	  List<Encounter> listEncounter = new ArrayList<Encounter>();
	  int enMin=0,ecMax=100;
	  {
		  int limit=50;
		  int i=0;
		  while (i<limit) {
			  Encounter encounter = new Encounter();
			  encounter.id=UUID.randomUUID().toString();
			  encounter.encounterType=encounterType[getRandom(0, 5)];
			  encounter.patientId=((Patient)listPatient.get(getRandom(ptMin, ptMax))).id;
			  encounter.practitionerId=((Practitioner)listPractitioner.get(getRandom(prMin, prMax))).id;
			  encounter.careEpisode="HealthEvaluation-"+i;
			  encounter.diagnosis="Diagnosis-"+i;
			  encounter.history="History-"+i;
			  encounter.notes="Notes notes notes ... for " + i;
			  encounter.participantMode="Primary";
			  encounter.procedureCode="SNOWMED Code";
			  encounter.reasonCode="Reason Code...";
			  encounter.reasonReference="Reason reference ...";
			  encounter.serviceProviderId=((Facility)listFacility.get(getRandom(lcMin, lcMax))).id;
			  encounter.language="English";
			  encounter.locationId=encounter.serviceProviderId;
			  encounter.status="Active";
			  encounter.encounterStartTime=new Timestamp(now.getTime()- 3600000); // now minus 60 minutes
			  encounter.encounterEndTime=now;
			  encounter.lastUpdatedTime=now;
			  
			  listEncounter.add(encounter);
			  i++;
		  }
		  for (Encounter encounter : listEncounter) {
			  buffer.append(encounter.getSql()+"\n");
			  System.out.println (encounter.getSql());
		  }	 		  
	  }	 
	  
	  // Write all SQL statements into .sql file
	  
	  BufferedWriter writer = new BufferedWriter(new FileWriter(new File("ehrsampledata.sql")));
	  writer.write(buffer.toString());
	  writer.flush();
	  writer.close();
  }
  
  public static int getRandom(int min, int max) {
	    Random random = new Random();
	    return random.nextInt(max - min) + min;
  } 
  
  
  public static long getDateInMillies (int year, int month, int date) {
	  GregorianCalendar gc = new GregorianCalendar (year, month, date);
	  return (gc.getTimeInMillis());
  }
  
}



class Patient {
	public Integer disabilityAdjYrs, qualityAdjYrs;
	public Date birthDate;
	public Timestamp deceasedDate, registeredOn, lastUpdatedTime;
	public String id, givenName, firstName, lastName, email, gender, sex, race, mothersMaidenName, isMarried, phoneNumber, language, abhaNumber, mrn, dlNumber, passportNumber, registeredAt, isDeceased;
	
	public String getSql () {
		String sql = "insert into PATIENT (id, given_name, first_name, last_name, email, gender, sex, race, mothers_maiden_name, birth_date, disability_adj_yrs, quality_adj_yrs , isMarried, phone_number, language, abha_number, mrn, dl_number, passport_number, registered_on, registered_At, is_deceased, last_updatedtime) values "
				+ "                       ('"+id+"', '"+givenName+"', '"+firstName+"', '"+lastName+"', '"+email+"', '"+gender+"', '"+sex+"', '"+race+"', '"+mothersMaidenName+"', '"+birthDate+"', "+disabilityAdjYrs+", "+qualityAdjYrs+", '"+isMarried+"', '"+phoneNumber+"', '"+language+"', '"+abhaNumber+"', '"+mrn+"', '"+dlNumber+"', '"+passportNumber+"', '"+registeredOn+"', '"+registeredAt+"', '"+isDeceased+"', '"+lastUpdatedTime+"');";
		return (sql);		 
	}
}

/**
 * Keep 5 locations
 *
 */
class Location {
	public Timestamp lastUpdatedTime;
	public String id, name, addressLine1, addressLine2, city, state, country, postCode, lattitude, longitude;
	public String getSql () {
		String sql = "insert into LOCATION (id, name, addressline_1, addressline_2, city, state, country, post_code, lattitude, longitude, last_updatedtime) values "
				+ "                       ('"+id+"', '"+name+"', '"+addressLine1+"', '"+addressLine2+"', '"+city+"', '"+state+"', '"+country+"', '"+postCode+"', '"+lattitude+"', '"+longitude+"', '"+lastUpdatedTime+"');";
		return (sql);		 
	}	
	
}

class Facility {
	/**
	 * locationId refers to id of Location table
	 * facilityType can be clinic, hospital, nursing home, laboratory, critical care
	 */
	
	public String id, name, locationId, type;
	public Timestamp lastUpdatedTime;
	public String getSql () {
		String sql = "insert into FACILITY (id, name, location_id, type, last_updatedtime) values "
				+ "                       ('"+id+"', '"+name+"', '"+locationId+"', '"+type+"', '"+lastUpdatedTime+"');";
		return (sql);		 
	}		
}

class Practitioner {
	/**
	 * General physician, Surgeon
	 * Specialization - Endocrinologist, Orthepedics, Orthodontist 
	 * primaryFacility refers to id of Facility table (Where doctor is available)
	 */
	public Date birthDate;
	public Timestamp lastUpdatedTime;
	public String id, givenName, firstName, lastName, email, gender, sex, aadhaarId, pan, passportNumber, specialization, phoneNumber, primaryLocation, qualification, language, organizationId;
	public String getSql () {
		String sql = "insert into PRACTITIONER (id, given_name, first_name, last_name, email, gender, sex, aadhaar_id, pan, passport_number, specialization, phone_number , primary_location, qualification, language, organization_id, last_updatedtime) values "
				+ "                       ('"+id+"', '"+givenName+"', '"+firstName+"', '"+lastName+"', '"+email+"', '"+gender+"', '"+sex+"', '"+aadhaarId+"', '"+pan+"', '"+passportNumber+"', '"+specialization+"', '"+phoneNumber+"', '"+primaryLocation+"', '"+qualification+"', '"+language+"', '"+organizationId+"', '"+lastUpdatedTime+"');";
		return (sql);		 
	}
}

class Encounter {
    public Timestamp encounterStartTime, encounterEndTime,lastUpdatedTime;
    /**
     * participantMode - primary or secondary
     * procedureCode - SNOWMED code
     * locationId refers to id of Location table (Where encounter has occurred,which facility)
     * serviceProviderId refers to OrganizationId through which service is provided
     */
	public String id, encounterType, language, notes, history, patientId, practitionerId, participantMode, careEpisode, reasonCode, reasonReference, diagnosis, procedureCode, locationId, status, serviceProviderId;
	public String getSql () {
		String sql = "insert into ENCOUNTER (id, encounter_type, language , notes, history, patient_id, practitioner_id, participant_mode, care_episode, reason_code, reason_reference, diagnosis, procedure_code, location_id, status, service_provider_id, enc_start_time, enc_end_time, last_updatedtime) values "
				+ "                       ('"+id+"', '"+encounterType+"', '"+language+"', '"+notes+"', '"+history+"', '"+patientId+"', '"+practitionerId+"', '"+participantMode+"', '"+careEpisode+"', '"+reasonCode+"', '"+reasonReference+"', '"+diagnosis+"', '"+procedureCode+"', '"+locationId+"', '"+status+"', '"+serviceProviderId+"', '"+encounterStartTime+"', '"+encounterEndTime+"', '"+lastUpdatedTime+"');";
		return (sql);		 
	}	
}
