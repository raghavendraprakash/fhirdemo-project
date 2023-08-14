#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-01-13.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json
import six
from fhir.resources import activitydefinition
from fhir.resources.fhirdate import FHIRDate

from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ActivityDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ActivityDefinition", js["resourceType"])
        return activitydefinition.ActivityDefinition(js)
    
    def testActivityDefinition1(self):
        inst = self.instantiate_from("activitydefinition-predecessor-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ActivityDefinition instance")
        self.implActivityDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("ActivityDefinition", js["resourceType"])
        inst2 = activitydefinition.ActivityDefinition(js)
        self.implActivityDefinition1(inst2)
    
    def implActivityDefinition1(self, inst):
        self.assertEqual(inst.approvalDate.date, FHIRDate("2016-03-12").date)
        self.assertEqual(inst.approvalDate.as_json(), "2016-03-12")
        self.assertEqual(force_bytes(inst.author[0].name), force_bytes("Motive Medical Intelligence"))
        self.assertEqual(force_bytes(inst.author[0].telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.author[0].telecom[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.author[0].telecom[0].value), force_bytes("415-362-4007"))
        self.assertEqual(force_bytes(inst.author[0].telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.author[0].telecom[1].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.author[0].telecom[1].value), force_bytes("info@motivemi.com"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("306206005"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Referral to service (procedure)"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("415-362-4007"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[1].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[1].value), force_bytes("info@motivemi.com"))
        self.assertEqual(force_bytes(inst.copyright), force_bytes("© Copyright 2016 Motive Medical Intelligence. All rights reserved."))
        self.assertEqual(inst.date.date, FHIRDate("2017-03-03T14:06:00Z").date)
        self.assertEqual(inst.date.as_json(), "2017-03-03T14:06:00Z")
        self.assertEqual(force_bytes(inst.description), force_bytes("refer to primary care mental-health integrated care program for evaluation and treatment of mental health conditions now"))
        self.assertEqual(inst.effectivePeriod.end.date, FHIRDate("2017-12-31").date)
        self.assertEqual(inst.effectivePeriod.end.as_json(), "2017-12-31")
        self.assertEqual(inst.effectivePeriod.start.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2016-01-01")
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("referralPrimaryCareMentalHealth-initial"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://motivemi.com/artifacts"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("referralPrimaryCareMentalHealth"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].system), force_bytes("urn:iso:std:iso:3166"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("ServiceRequest"))
        self.assertEqual(inst.lastReviewDate.date, FHIRDate("2016-08-15").date)
        self.assertEqual(inst.lastReviewDate.as_json(), "2016-08-15")
        self.assertEqual(force_bytes(inst.name), force_bytes("ReferralPrimaryCareMentalHealth"))
        self.assertEqual(force_bytes(inst.participant[0].type), force_bytes("practitioner"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("Motive Medical Intelligence"))
        self.assertEqual(force_bytes(inst.relatedArtifact[0].display), force_bytes("Practice Guideline for the Treatment of Patients with Major Depressive Disorder"))
        self.assertEqual(force_bytes(inst.relatedArtifact[0].type), force_bytes("citation"))
        self.assertEqual(force_bytes(inst.relatedArtifact[0].url), force_bytes("http://psychiatryonline.org/pb/assets/raw/sitewide/practice_guidelines/guidelines/mdd.pdf"))
        self.assertEqual(force_bytes(inst.relatedArtifact[1].resource), force_bytes("ActivityDefinition/referralPrimaryCareMentalHealth"))
        self.assertEqual(force_bytes(inst.relatedArtifact[1].type), force_bytes("successor"))
        self.assertEqual(force_bytes(inst.status), force_bytes("retired"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Referral to Primary Care Mental Health"))
        self.assertEqual(force_bytes(inst.topic[0].text), force_bytes("Mental Health Referral"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://motivemi.com/artifacts/ActivityDefinition/referralPrimaryCareMentalHealth"))
        self.assertEqual(force_bytes(inst.useContext[0].code.code), force_bytes("age"))
        self.assertEqual(force_bytes(inst.useContext[0].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code), force_bytes("D000328"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].display), force_bytes("Adult"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system), force_bytes("https://meshb.nlm.nih.gov"))
        self.assertEqual(force_bytes(inst.useContext[1].code.code), force_bytes("focus"))
        self.assertEqual(force_bytes(inst.useContext[1].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].code), force_bytes("87512008"))
        self.assertEqual(force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].display), force_bytes("Mild major depression"))
        self.assertEqual(force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.useContext[2].code.code), force_bytes("focus"))
        self.assertEqual(force_bytes(inst.useContext[2].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[2].valueCodeableConcept.coding[0].code), force_bytes("40379007"))
        self.assertEqual(force_bytes(inst.useContext[2].valueCodeableConcept.coding[0].display), force_bytes("Major depression, recurrent, mild"))
        self.assertEqual(force_bytes(inst.useContext[2].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.useContext[3].code.code), force_bytes("focus"))
        self.assertEqual(force_bytes(inst.useContext[3].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[3].valueCodeableConcept.coding[0].code), force_bytes("225444004"))
        self.assertEqual(force_bytes(inst.useContext[3].valueCodeableConcept.coding[0].display), force_bytes("At risk for suicide (finding)"))
        self.assertEqual(force_bytes(inst.useContext[3].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.useContext[4].code.code), force_bytes("focus"))
        self.assertEqual(force_bytes(inst.useContext[4].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[4].valueCodeableConcept.coding[0].code), force_bytes("306206005"))
        self.assertEqual(force_bytes(inst.useContext[4].valueCodeableConcept.coding[0].display), force_bytes("Referral to service (procedure)"))
        self.assertEqual(force_bytes(inst.useContext[4].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.useContext[5].code.code), force_bytes("user"))
        self.assertEqual(force_bytes(inst.useContext[5].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[5].valueCodeableConcept.coding[0].code), force_bytes("309343006"))
        self.assertEqual(force_bytes(inst.useContext[5].valueCodeableConcept.coding[0].display), force_bytes("Physician"))
        self.assertEqual(force_bytes(inst.useContext[5].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.useContext[6].code.code), force_bytes("venue"))
        self.assertEqual(force_bytes(inst.useContext[6].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[6].valueCodeableConcept.coding[0].code), force_bytes("440655000"))
        self.assertEqual(force_bytes(inst.useContext[6].valueCodeableConcept.coding[0].display), force_bytes("Outpatient environment"))
        self.assertEqual(force_bytes(inst.useContext[6].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))
    
    def testActivityDefinition2(self):
        inst = self.instantiate_from("activitydefinition-supplyrequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ActivityDefinition instance")
        self.implActivityDefinition2(inst)
        
        js = inst.as_json()
        self.assertEqual("ActivityDefinition", js["resourceType"])
        inst2 = activitydefinition.ActivityDefinition(js)
        self.implActivityDefinition2(inst2)
    
    def implActivityDefinition2(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("BlueTubes"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Blood collect tubes blue cap"))
        self.assertEqual(force_bytes(inst.description), force_bytes("10 Blood collect tubes blue cap"))
        self.assertEqual(force_bytes(inst.id), force_bytes("blood-tubes-supply"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("SupplyRequest"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.purpose), force_bytes("Describes a request for 10 Blood collection tubes with blue caps."))
        self.assertEqual(inst.quantity.value, 10)
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.transform), force_bytes("StructureMap/supplyrequest-transform"))
    
    def testActivityDefinition3(self):
        inst = self.instantiate_from("activitydefinition-servicerequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ActivityDefinition instance")
        self.implActivityDefinition3(inst)
        
        js = inst.as_json()
        self.assertEqual("ActivityDefinition", js["resourceType"])
        inst2 = activitydefinition.ActivityDefinition(js)
        self.implActivityDefinition3(inst2)
    
    def implActivityDefinition3(self, inst):
        self.assertEqual(force_bytes(inst.bodySite[0].coding[0].code), force_bytes("17401000"))
        self.assertEqual(force_bytes(inst.bodySite[0].coding[0].display), force_bytes("Heart valve structure"))
        self.assertEqual(force_bytes(inst.bodySite[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("34068001"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Heart valve replacement"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.description), force_bytes("Heart valve replacement"))
        self.assertEqual(force_bytes(inst.id), force_bytes("heart-valve-replacement"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("ServiceRequest"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.participant[0].role.coding[0].code), force_bytes("207RI0011X"))
        self.assertEqual(force_bytes(inst.participant[0].role.coding[0].display), force_bytes("Interventional Cardiology"))
        self.assertEqual(force_bytes(inst.participant[0].role.coding[0].system), force_bytes("http://nucc.org/provider-taxonomy"))
        self.assertEqual(force_bytes(inst.participant[0].role.text), force_bytes("Interventional Cardiology"))
        self.assertEqual(force_bytes(inst.participant[0].type), force_bytes("practitioner"))
        self.assertEqual(force_bytes(inst.purpose), force_bytes("Describes the proposal to perform a Heart Valve replacement."))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.topic[0].coding[0].code), force_bytes("34068001"))
        self.assertEqual(force_bytes(inst.topic[0].coding[0].display), force_bytes("Heart valve replacement"))
        self.assertEqual(force_bytes(inst.topic[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.useContext[0].code.code), force_bytes("age"))
        self.assertEqual(force_bytes(inst.useContext[0].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code), force_bytes("D000328"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].display), force_bytes("Adult"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system), force_bytes("https://meshb.nlm.nih.gov"))
        self.assertEqual(force_bytes(inst.useContext[1].code.code), force_bytes("user"))
        self.assertEqual(force_bytes(inst.useContext[1].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].code), force_bytes("309343006"))
        self.assertEqual(force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].display), force_bytes("Physician"))
        self.assertEqual(force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
    
    def testActivityDefinition4(self):
        inst = self.instantiate_from("activitydefinition-medicationorder-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ActivityDefinition instance")
        self.implActivityDefinition4(inst)
        
        js = inst.as_json()
        self.assertEqual("ActivityDefinition", js["resourceType"])
        inst2 = activitydefinition.ActivityDefinition(js)
        self.implActivityDefinition4(inst2)
    
    def implActivityDefinition4(self, inst):
        self.assertEqual(inst.approvalDate.date, FHIRDate("2016-03-12").date)
        self.assertEqual(inst.approvalDate.as_json(), "2016-03-12")
        self.assertEqual(force_bytes(inst.author[0].name), force_bytes("Motive Medical Intelligence"))
        self.assertEqual(force_bytes(inst.author[0].telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.author[0].telecom[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.author[0].telecom[0].value), force_bytes("415-362-4007"))
        self.assertEqual(force_bytes(inst.author[0].telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.author[0].telecom[1].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.author[0].telecom[1].value), force_bytes("info@motivemi.com"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("415-362-4007"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[1].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[1].value), force_bytes("info@motivemi.com"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("citalopramMedication"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("citalopramSubstance"))
        self.assertEqual(force_bytes(inst.copyright), force_bytes("© Copyright 2016 Motive Medical Intelligence. All rights reserved."))
        self.assertEqual(inst.date.date, FHIRDate("2015-08-15").date)
        self.assertEqual(inst.date.as_json(), "2015-08-15")
        self.assertEqual(force_bytes(inst.description), force_bytes("Citalopram 20 mg tablet 1 tablet oral 1 time daily now (30 table; 3 refills"))
        self.assertEqual(force_bytes(inst.dosage[0].doseAndRate[0].doseQuantity.unit), force_bytes("{tbl}"))
        self.assertEqual(inst.dosage[0].doseAndRate[0].doseQuantity.value, 1)
        self.assertEqual(force_bytes(inst.dosage[0].doseAndRate[0].type.coding[0].code), force_bytes("ordered"))
        self.assertEqual(force_bytes(inst.dosage[0].doseAndRate[0].type.coding[0].display), force_bytes("Ordered"))
        self.assertEqual(force_bytes(inst.dosage[0].doseAndRate[0].type.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/dose-rate-type"))
        self.assertEqual(force_bytes(inst.dosage[0].route.coding[0].code), force_bytes("26643006"))
        self.assertEqual(force_bytes(inst.dosage[0].route.coding[0].display), force_bytes("Oral route (qualifier value)"))
        self.assertEqual(force_bytes(inst.dosage[0].route.text), force_bytes("Oral route (qualifier value)"))
        self.assertEqual(force_bytes(inst.dosage[0].text), force_bytes("1 tablet oral 1 time daily"))
        self.assertEqual(inst.dosage[0].timing.repeat.frequency, 1)
        self.assertEqual(inst.dosage[0].timing.repeat.period, 1)
        self.assertEqual(force_bytes(inst.dosage[0].timing.repeat.periodUnit), force_bytes("d"))
        self.assertEqual(force_bytes(inst.dynamicValue[0].expression.description), force_bytes("dispenseRequest.numberOfRepeatsAllowed is three (3)"))
        self.assertEqual(force_bytes(inst.dynamicValue[0].expression.expression), force_bytes("3"))
        self.assertEqual(force_bytes(inst.dynamicValue[0].expression.language), force_bytes("text/cql"))
        self.assertEqual(force_bytes(inst.dynamicValue[0].path), force_bytes("dispenseRequest.numberOfRepeatsAllowed"))
        self.assertEqual(force_bytes(inst.dynamicValue[1].expression.description), force_bytes("dispenseRequest.quantity is thirty (30) tablets"))
        self.assertEqual(force_bytes(inst.dynamicValue[1].expression.expression), force_bytes("30 '{tbl}'"))
        self.assertEqual(force_bytes(inst.dynamicValue[1].expression.language), force_bytes("text/cql"))
        self.assertEqual(force_bytes(inst.dynamicValue[1].path), force_bytes("dispenseRequest.quantity"))
        self.assertEqual(inst.effectivePeriod.end.date, FHIRDate("2017-12-31").date)
        self.assertEqual(inst.effectivePeriod.end.as_json(), "2017-12-31")
        self.assertEqual(inst.effectivePeriod.start.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2016-01-01")
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("citalopramPrescription"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://motivemi.com"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("citalopramPrescription"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].system), force_bytes("urn:iso:std:iso:3166"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("MedicationRequest"))
        self.assertEqual(inst.lastReviewDate.date, FHIRDate("2016-08-15").date)
        self.assertEqual(inst.lastReviewDate.as_json(), "2016-08-15")
        self.assertEqual(force_bytes(inst.name), force_bytes("CitalopramPrescription"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("Motive Medical Intelligence"))
        self.assertEqual(force_bytes(inst.purpose), force_bytes("Defines a guideline supported prescription for the treatment of depressive disorders"))
        self.assertEqual(force_bytes(inst.relatedArtifact[0].display), force_bytes("Practice Guideline for the Treatment of Patients with Major Depressive Disorder"))
        self.assertEqual(force_bytes(inst.relatedArtifact[0].type), force_bytes("citation"))
        self.assertEqual(force_bytes(inst.relatedArtifact[0].url), force_bytes("http://psychiatryonline.org/pb/assets/raw/sitewide/practice_guidelines/guidelines/mdd.pdf"))
        self.assertEqual(force_bytes(inst.relatedArtifact[1].resource), force_bytes("#citalopramMedication"))
        self.assertEqual(force_bytes(inst.relatedArtifact[1].type), force_bytes("composed-of"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Citalopram Prescription"))
        self.assertEqual(force_bytes(inst.topic[0].text), force_bytes("Mental Health Treatment"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://motivemi.com/artifacts/ActivityDefinition/citalopramPrescription"))
        self.assertEqual(force_bytes(inst.usage), force_bytes("This activity definition is used as part of various suicide risk order sets"))
        self.assertEqual(force_bytes(inst.useContext[0].code.code), force_bytes("age"))
        self.assertEqual(force_bytes(inst.useContext[0].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code), force_bytes("D000328"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].display), force_bytes("Adult"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system), force_bytes("https://meshb.nlm.nih.gov"))
        self.assertEqual(force_bytes(inst.useContext[1].code.code), force_bytes("focus"))
        self.assertEqual(force_bytes(inst.useContext[1].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].code), force_bytes("87512008"))
        self.assertEqual(force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].display), force_bytes("Mild major depression"))
        self.assertEqual(force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.useContext[2].code.code), force_bytes("focus"))
        self.assertEqual(force_bytes(inst.useContext[2].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[2].valueCodeableConcept.coding[0].code), force_bytes("40379007"))
        self.assertEqual(force_bytes(inst.useContext[2].valueCodeableConcept.coding[0].display), force_bytes("Major depression, recurrent, mild"))
        self.assertEqual(force_bytes(inst.useContext[2].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.useContext[3].code.code), force_bytes("focus"))
        self.assertEqual(force_bytes(inst.useContext[3].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[3].valueCodeableConcept.coding[0].code), force_bytes("225444004"))
        self.assertEqual(force_bytes(inst.useContext[3].valueCodeableConcept.coding[0].display), force_bytes("At risk for suicide (finding)"))
        self.assertEqual(force_bytes(inst.useContext[3].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.useContext[4].code.code), force_bytes("focus"))
        self.assertEqual(force_bytes(inst.useContext[4].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[4].valueCodeableConcept.coding[0].code), force_bytes("306206005"))
        self.assertEqual(force_bytes(inst.useContext[4].valueCodeableConcept.coding[0].display), force_bytes("Referral to service (procedure)"))
        self.assertEqual(force_bytes(inst.useContext[4].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.useContext[5].code.code), force_bytes("user"))
        self.assertEqual(force_bytes(inst.useContext[5].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[5].valueCodeableConcept.coding[0].code), force_bytes("309343006"))
        self.assertEqual(force_bytes(inst.useContext[5].valueCodeableConcept.coding[0].display), force_bytes("Physician"))
        self.assertEqual(force_bytes(inst.useContext[5].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.useContext[6].code.code), force_bytes("venue"))
        self.assertEqual(force_bytes(inst.useContext[6].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[6].valueCodeableConcept.coding[0].code), force_bytes("440655000"))
        self.assertEqual(force_bytes(inst.useContext[6].valueCodeableConcept.coding[0].display), force_bytes("Outpatient environment"))
        self.assertEqual(force_bytes(inst.useContext[6].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))
    
    def testActivityDefinition5(self):
        inst = self.instantiate_from("activitydefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ActivityDefinition instance")
        self.implActivityDefinition5(inst)
        
        js = inst.as_json()
        self.assertEqual("ActivityDefinition", js["resourceType"])
        inst2 = activitydefinition.ActivityDefinition(js)
        self.implActivityDefinition5(inst2)
    
    def implActivityDefinition5(self, inst):
        self.assertEqual(inst.approvalDate.date, FHIRDate("2017-03-01").date)
        self.assertEqual(inst.approvalDate.as_json(), "2017-03-01")
        self.assertEqual(force_bytes(inst.author[0].name), force_bytes("Motive Medical Intelligence"))
        self.assertEqual(force_bytes(inst.author[0].telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.author[0].telecom[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.author[0].telecom[0].value), force_bytes("415-362-4007"))
        self.assertEqual(force_bytes(inst.author[0].telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.author[0].telecom[1].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.author[0].telecom[1].value), force_bytes("info@motivemi.com"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("306206005"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Referral to service (procedure)"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("415-362-4007"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[1].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[1].value), force_bytes("info@motivemi.com"))
        self.assertEqual(force_bytes(inst.copyright), force_bytes("© Copyright 2016 Motive Medical Intelligence. All rights reserved."))
        self.assertEqual(inst.date.date, FHIRDate("2017-03-03T14:06:00Z").date)
        self.assertEqual(inst.date.as_json(), "2017-03-03T14:06:00Z")
        self.assertEqual(force_bytes(inst.description), force_bytes("refer to primary care mental-health integrated care program for evaluation and treatment of mental health conditions now"))
        self.assertEqual(inst.effectivePeriod.end.date, FHIRDate("2017-12-31").date)
        self.assertEqual(inst.effectivePeriod.end.as_json(), "2017-12-31")
        self.assertEqual(inst.effectivePeriod.start.date, FHIRDate("2017-03-01").date)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2017-03-01")
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.id), force_bytes("referralPrimaryCareMentalHealth"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://motivemi.com/artifacts"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("referralPrimaryCareMentalHealth"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].system), force_bytes("urn:iso:std:iso:3166"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("ServiceRequest"))
        self.assertEqual(inst.lastReviewDate.date, FHIRDate("2017-03-01").date)
        self.assertEqual(inst.lastReviewDate.as_json(), "2017-03-01")
        self.assertEqual(force_bytes(inst.name), force_bytes("ReferralPrimaryCareMentalHealth"))
        self.assertEqual(force_bytes(inst.participant[0].type), force_bytes("practitioner"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("Motive Medical Intelligence"))
        self.assertEqual(force_bytes(inst.relatedArtifact[0].display), force_bytes("Practice Guideline for the Treatment of Patients with Major Depressive Disorder"))
        self.assertEqual(force_bytes(inst.relatedArtifact[0].type), force_bytes("citation"))
        self.assertEqual(force_bytes(inst.relatedArtifact[0].url), force_bytes("http://psychiatryonline.org/pb/assets/raw/sitewide/practice_guidelines/guidelines/mdd.pdf"))
        self.assertEqual(force_bytes(inst.relatedArtifact[1].resource), force_bytes("ActivityDefinition/referralPrimaryCareMentalHealth-initial"))
        self.assertEqual(force_bytes(inst.relatedArtifact[1].type), force_bytes("predecessor"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Referral to Primary Care Mental Health"))
        self.assertEqual(force_bytes(inst.topic[0].text), force_bytes("Mental Health Referral"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://motivemi.com/artifacts/ActivityDefinition/referralPrimaryCareMentalHealth"))
        self.assertEqual(force_bytes(inst.useContext[0].code.code), force_bytes("age"))
        self.assertEqual(force_bytes(inst.useContext[0].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code), force_bytes("D000328"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].display), force_bytes("Adult"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system), force_bytes("https://meshb.nlm.nih.gov"))
        self.assertEqual(force_bytes(inst.useContext[1].code.code), force_bytes("focus"))
        self.assertEqual(force_bytes(inst.useContext[1].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].code), force_bytes("87512008"))
        self.assertEqual(force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].display), force_bytes("Mild major depression"))
        self.assertEqual(force_bytes(inst.useContext[1].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.useContext[2].code.code), force_bytes("focus"))
        self.assertEqual(force_bytes(inst.useContext[2].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[2].valueCodeableConcept.coding[0].code), force_bytes("40379007"))
        self.assertEqual(force_bytes(inst.useContext[2].valueCodeableConcept.coding[0].display), force_bytes("Major depression, recurrent, mild"))
        self.assertEqual(force_bytes(inst.useContext[2].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.useContext[3].code.code), force_bytes("focus"))
        self.assertEqual(force_bytes(inst.useContext[3].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[3].valueCodeableConcept.coding[0].code), force_bytes("225444004"))
        self.assertEqual(force_bytes(inst.useContext[3].valueCodeableConcept.coding[0].display), force_bytes("At risk for suicide (finding)"))
        self.assertEqual(force_bytes(inst.useContext[3].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.useContext[4].code.code), force_bytes("focus"))
        self.assertEqual(force_bytes(inst.useContext[4].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[4].valueCodeableConcept.coding[0].code), force_bytes("306206005"))
        self.assertEqual(force_bytes(inst.useContext[4].valueCodeableConcept.coding[0].display), force_bytes("Referral to service (procedure)"))
        self.assertEqual(force_bytes(inst.useContext[4].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.useContext[5].code.code), force_bytes("user"))
        self.assertEqual(force_bytes(inst.useContext[5].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[5].valueCodeableConcept.coding[0].code), force_bytes("309343006"))
        self.assertEqual(force_bytes(inst.useContext[5].valueCodeableConcept.coding[0].display), force_bytes("Physician"))
        self.assertEqual(force_bytes(inst.useContext[5].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.useContext[6].code.code), force_bytes("venue"))
        self.assertEqual(force_bytes(inst.useContext[6].code.system), force_bytes("http://terminology.hl7.org/CodeSystem/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[6].valueCodeableConcept.coding[0].code), force_bytes("440655000"))
        self.assertEqual(force_bytes(inst.useContext[6].valueCodeableConcept.coding[0].display), force_bytes("Outpatient environment"))
        self.assertEqual(force_bytes(inst.useContext[6].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.version), force_bytes("1.1.0"))

