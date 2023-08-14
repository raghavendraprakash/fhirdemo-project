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
from fhir.resources import immunization
from fhir.resources.fhirdate import FHIRDate

from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ImmunizationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Immunization", js["resourceType"])
        return immunization.Immunization(js)
    
    def testImmunization1(self):
        inst = self.instantiate_from("immunization-example-subpotent.json")
        self.assertIsNotNone(inst, "Must have instantiated a Immunization instance")
        self.implImmunization1(inst)
        
        js = inst.as_json()
        self.assertEqual("Immunization", js["resourceType"])
        inst2 = immunization.Immunization(js)
        self.implImmunization1(inst2)
    
    def implImmunization1(self, inst):
        self.assertEqual(force_bytes(inst.doseQuantity.code), force_bytes("ml"))
        self.assertEqual(force_bytes(inst.doseQuantity.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(inst.doseQuantity.value, 0.5)
        self.assertEqual(force_bytes(inst.education[0].documentType), force_bytes("253088698300010311120702"))
        self.assertEqual(inst.education[0].presentationDate.date, FHIRDate("2013-01-10").date)
        self.assertEqual(inst.education[0].presentationDate.as_json(), "2013-01-10")
        self.assertEqual(inst.education[0].publicationDate.date, FHIRDate("2012-07-02").date)
        self.assertEqual(inst.education[0].publicationDate.as_json(), "2012-07-02")
        self.assertEqual(inst.expirationDate.date, FHIRDate("2015-02-28").date)
        self.assertEqual(inst.expirationDate.as_json(), "2015-02-28")
        self.assertEqual(force_bytes(inst.fundingSource.coding[0].code), force_bytes("private"))
        self.assertEqual(force_bytes(inst.fundingSource.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/immunization-funding-source"))
        self.assertEqual(force_bytes(inst.id), force_bytes("subpotent"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"))
        self.assertFalse(inst.isSubpotent)
        self.assertEqual(force_bytes(inst.lotNumber), force_bytes("AAJN11K"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.note[0].text), force_bytes("Notes on adminstration of vaccine"))
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2015-01-15").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2015-01-15")
        self.assertEqual(force_bytes(inst.performer[0].function.coding[0].code), force_bytes("OP"))
        self.assertEqual(force_bytes(inst.performer[0].function.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0443"))
        self.assertEqual(force_bytes(inst.performer[1].function.coding[0].code), force_bytes("AP"))
        self.assertEqual(force_bytes(inst.performer[1].function.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0443"))
        self.assertTrue(inst.primarySource)
        self.assertEqual(force_bytes(inst.programEligibility[0].coding[0].code), force_bytes("ineligible"))
        self.assertEqual(force_bytes(inst.programEligibility[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/immunization-program-eligibility"))
        self.assertEqual(force_bytes(inst.route.coding[0].code), force_bytes("IM"))
        self.assertEqual(force_bytes(inst.route.coding[0].display), force_bytes("Injection, intramuscular"))
        self.assertEqual(force_bytes(inst.route.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration"))
        self.assertEqual(force_bytes(inst.site.coding[0].code), force_bytes("LT"))
        self.assertEqual(force_bytes(inst.site.coding[0].display), force_bytes("left thigh"))
        self.assertEqual(force_bytes(inst.site.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActSite"))
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.subpotentReason[0].coding[0].code), force_bytes("partial"))
        self.assertEqual(force_bytes(inst.subpotentReason[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/immunization-subpotent-reason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.vaccineCode.coding[0].code), force_bytes("GNHEP"))
        self.assertEqual(force_bytes(inst.vaccineCode.coding[0].system), force_bytes("urn:oid:1.2.36.1.2001.1005.17"))
        self.assertEqual(force_bytes(inst.vaccineCode.text), force_bytes("Hepatitis B"))
    
    def testImmunization2(self):
        inst = self.instantiate_from("immunization-example-protocol.json")
        self.assertIsNotNone(inst, "Must have instantiated a Immunization instance")
        self.implImmunization2(inst)
        
        js = inst.as_json()
        self.assertEqual("Immunization", js["resourceType"])
        inst2 = immunization.Immunization(js)
        self.implImmunization2(inst2)
    
    def implImmunization2(self, inst):
        self.assertEqual(force_bytes(inst.doseQuantity.code), force_bytes("mg"))
        self.assertEqual(force_bytes(inst.doseQuantity.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(inst.doseQuantity.value, 5)
        self.assertEqual(inst.expirationDate.date, FHIRDate("2018-12-15").date)
        self.assertEqual(inst.expirationDate.as_json(), "2018-12-15")
        self.assertEqual(force_bytes(inst.fundingSource.coding[0].code), force_bytes("private"))
        self.assertEqual(force_bytes(inst.fundingSource.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/immunization-funding-source"))
        self.assertEqual(force_bytes(inst.id), force_bytes("protocol"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"))
        self.assertFalse(inst.isSubpotent)
        self.assertEqual(force_bytes(inst.lotNumber), force_bytes("PT123F"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2018-06-18").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2018-06-18")
        self.assertEqual(force_bytes(inst.performer[0].function.coding[0].code), force_bytes("OP"))
        self.assertEqual(force_bytes(inst.performer[0].function.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0443"))
        self.assertEqual(force_bytes(inst.performer[1].function.coding[0].code), force_bytes("AP"))
        self.assertEqual(force_bytes(inst.performer[1].function.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0443"))
        self.assertTrue(inst.primarySource)
        self.assertEqual(force_bytes(inst.programEligibility[0].coding[0].code), force_bytes("ineligible"))
        self.assertEqual(force_bytes(inst.programEligibility[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/immunization-program-eligibility"))
        self.assertEqual(inst.protocolApplied[0].doseNumberPositiveInt, 1)
        self.assertEqual(force_bytes(inst.protocolApplied[0].series), force_bytes("2-dose"))
        self.assertEqual(force_bytes(inst.protocolApplied[0].targetDisease[0].coding[0].code), force_bytes("40468003"))
        self.assertEqual(force_bytes(inst.protocolApplied[0].targetDisease[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(inst.protocolApplied[1].doseNumberPositiveInt, 2)
        self.assertEqual(force_bytes(inst.protocolApplied[1].series), force_bytes("3-dose"))
        self.assertEqual(force_bytes(inst.protocolApplied[1].targetDisease[0].coding[0].code), force_bytes("66071002"))
        self.assertEqual(force_bytes(inst.protocolApplied[1].targetDisease[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.route.coding[0].code), force_bytes("IM"))
        self.assertEqual(force_bytes(inst.route.coding[0].display), force_bytes("Injection, intramuscular"))
        self.assertEqual(force_bytes(inst.route.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration"))
        self.assertEqual(force_bytes(inst.site.coding[0].code), force_bytes("LA"))
        self.assertEqual(force_bytes(inst.site.coding[0].display), force_bytes("left arm"))
        self.assertEqual(force_bytes(inst.site.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActSite"))
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.vaccineCode.coding[0].code), force_bytes("104"))
        self.assertEqual(force_bytes(inst.vaccineCode.coding[0].system), force_bytes("http://hl7.org/fhir/sid/cvx"))
        self.assertEqual(force_bytes(inst.vaccineCode.text), force_bytes("Twinrix (HepA/HepB)"))
    
    def testImmunization3(self):
        inst = self.instantiate_from("immunization-example-refused.json")
        self.assertIsNotNone(inst, "Must have instantiated a Immunization instance")
        self.implImmunization3(inst)
        
        js = inst.as_json()
        self.assertEqual("Immunization", js["resourceType"])
        inst2 = immunization.Immunization(js)
        self.implImmunization3(inst2)
    
    def implImmunization3(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("notGiven"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2013-01-10").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-01-10")
        self.assertTrue(inst.primarySource)
        self.assertEqual(force_bytes(inst.status), force_bytes("not-done"))
        self.assertEqual(force_bytes(inst.statusReason.coding[0].code), force_bytes("MEDPREC"))
        self.assertEqual(force_bytes(inst.statusReason.coding[0].display), force_bytes("medical precaution"))
        self.assertEqual(force_bytes(inst.statusReason.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.vaccineCode.coding[0].code), force_bytes("01"))
        self.assertEqual(force_bytes(inst.vaccineCode.coding[0].display), force_bytes("DTP"))
        self.assertEqual(force_bytes(inst.vaccineCode.coding[0].system), force_bytes("http://hl7.org/fhir/sid/cvx"))
    
    def testImmunization4(self):
        inst = self.instantiate_from("immunization-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Immunization instance")
        self.implImmunization4(inst)
        
        js = inst.as_json()
        self.assertEqual("Immunization", js["resourceType"])
        inst2 = immunization.Immunization(js)
        self.implImmunization4(inst2)
    
    def implImmunization4(self, inst):
        self.assertEqual(force_bytes(inst.doseQuantity.code), force_bytes("mg"))
        self.assertEqual(force_bytes(inst.doseQuantity.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(inst.doseQuantity.value, 5)
        self.assertEqual(force_bytes(inst.education[0].documentType), force_bytes("253088698300010311120702"))
        self.assertEqual(inst.education[0].presentationDate.date, FHIRDate("2013-01-10").date)
        self.assertEqual(inst.education[0].presentationDate.as_json(), "2013-01-10")
        self.assertEqual(inst.education[0].publicationDate.date, FHIRDate("2012-07-02").date)
        self.assertEqual(inst.education[0].publicationDate.as_json(), "2012-07-02")
        self.assertEqual(inst.expirationDate.date, FHIRDate("2015-02-15").date)
        self.assertEqual(inst.expirationDate.as_json(), "2015-02-15")
        self.assertEqual(force_bytes(inst.fundingSource.coding[0].code), force_bytes("private"))
        self.assertEqual(force_bytes(inst.fundingSource.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/immunization-funding-source"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"))
        self.assertTrue(inst.isSubpotent)
        self.assertEqual(force_bytes(inst.lotNumber), force_bytes("AAJN11K"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.note[0].text), force_bytes("Notes on adminstration of vaccine"))
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2013-01-10").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-01-10")
        self.assertEqual(force_bytes(inst.performer[0].function.coding[0].code), force_bytes("OP"))
        self.assertEqual(force_bytes(inst.performer[0].function.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0443"))
        self.assertEqual(force_bytes(inst.performer[1].function.coding[0].code), force_bytes("AP"))
        self.assertEqual(force_bytes(inst.performer[1].function.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v2-0443"))
        self.assertTrue(inst.primarySource)
        self.assertEqual(force_bytes(inst.programEligibility[0].coding[0].code), force_bytes("ineligible"))
        self.assertEqual(force_bytes(inst.programEligibility[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/immunization-program-eligibility"))
        self.assertEqual(force_bytes(inst.reasonCode[0].coding[0].code), force_bytes("429060002"))
        self.assertEqual(force_bytes(inst.reasonCode[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.route.coding[0].code), force_bytes("IM"))
        self.assertEqual(force_bytes(inst.route.coding[0].display), force_bytes("Injection, intramuscular"))
        self.assertEqual(force_bytes(inst.route.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration"))
        self.assertEqual(force_bytes(inst.site.coding[0].code), force_bytes("LA"))
        self.assertEqual(force_bytes(inst.site.coding[0].display), force_bytes("left arm"))
        self.assertEqual(force_bytes(inst.site.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActSite"))
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.vaccineCode.coding[0].code), force_bytes("FLUVAX"))
        self.assertEqual(force_bytes(inst.vaccineCode.coding[0].system), force_bytes("urn:oid:1.2.36.1.2001.1005.17"))
        self.assertEqual(force_bytes(inst.vaccineCode.text), force_bytes("Fluvax (Influenza)"))
    
    def testImmunization5(self):
        inst = self.instantiate_from("immunization-example-historical.json")
        self.assertIsNotNone(inst, "Must have instantiated a Immunization instance")
        self.implImmunization5(inst)
        
        js = inst.as_json()
        self.assertEqual("Immunization", js["resourceType"])
        inst2 = immunization.Immunization(js)
        self.implImmunization5(inst2)
    
    def implImmunization5(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("historical"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.note[0].text), force_bytes("Notes on adminstration of a historical vaccine"))
        self.assertEqual(force_bytes(inst.occurrenceString), force_bytes("January 2012"))
        self.assertFalse(inst.primarySource)
        self.assertEqual(force_bytes(inst.reportOrigin.coding[0].code), force_bytes("record"))
        self.assertEqual(force_bytes(inst.reportOrigin.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/immunization-origin"))
        self.assertEqual(force_bytes(inst.reportOrigin.text), force_bytes("Written Record"))
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.vaccineCode.coding[0].code), force_bytes("GNFLU"))
        self.assertEqual(force_bytes(inst.vaccineCode.coding[0].system), force_bytes("urn:oid:1.2.36.1.2001.1005.17"))
        self.assertEqual(force_bytes(inst.vaccineCode.text), force_bytes("Influenza"))

