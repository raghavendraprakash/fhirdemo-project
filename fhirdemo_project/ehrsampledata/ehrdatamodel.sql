create table PATIENT (
	id VARCHAR(50) primary key,
	given_name VARCHAR(50),
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	email VARCHAR(50),
	gender VARCHAR(50),
	sex VARCHAR(50),
	race VARCHAR(50),
	mothers_maiden_name VARCHAR(50),
	birth_date DATE,
	disability_adj_yrs INT,
	quality_adj_yrs  INT,
	isMarried VARCHAR(50),
	phone_number VARCHAR(50),
	language VARCHAR(50),
	abha_number VARCHAR(50),
	mrn VARCHAR(50),
	dl_number VARCHAR(50),
	passport_number VARCHAR(50),
	registered_on TIMESTAMP,
	registered_at VARCHAR(40),
	is_deceased VARCHAR(50),
	deceased_date TIMESTAMP,
	last_updatedtime TIMESTAMP
);

create table LOCATION (
	id VARCHAR(50) primary key,
    name VARCHAR(50),
	addressline_1 VARCHAR(50),
	addressline_2 VARCHAR(50),
	city VARCHAR(50),
	state VARCHAR(50),
	country VARCHAR(50),
	post_code VARCHAR(50),	
	lattitude VARCHAR(50),
	longitude VARCHAR(50),
	last_updatedtime TIMESTAMP
);

create table FACILITY (
	id VARCHAR(50) primary key,
	name VARCHAR(50),
	type VARCHAR(50),
	location_id VARCHAR(50),
	last_updatedtime TIMESTAMP
);

create table ENCOUNTER (
	id VARCHAR(50) primary key,
	encounter_type VARCHAR(50),
    language VARCHAR(50),
	notes VARCHAR(4000),
	history VARCHAR(4000),
	patient_id VARCHAR(50),
	practitioner_id VARCHAR(50),
	participant_mode VARCHAR(50),
	care_episode VARCHAR(200),
	reason_code VARCHAR(50),
	reason_reference VARCHAR(50),
	diagnosis VARCHAR(50),
	procedure_code VARCHAR(50),	
	location_id VARCHAR(50),
	status VARCHAR(50),
	service_provider_id VARCHAR(50),
	enc_start_time TIMESTAMP,
	enc_end_time TIMESTAMP,
	last_updatedtime TIMESTAMP
);

create table PRACTITIONER (
	id VARCHAR(50) primary key,
	given_name VARCHAR(50),
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	email VARCHAR(50),
	gender VARCHAR(50),
	sex VARCHAR(50),
	aadhaar_id VARCHAR(100),
	pan VARCHAR(100),
	passport_number VARCHAR(50),
	specialization VARCHAR(50),
	phone_number VARCHAR(50),
	primary_location VARCHAR(50),
	qualification VARCHAR(50),
	language VARCHAR(50),
	organization_id VARCHAR(50),
	last_updatedtime TIMESTAMP
);