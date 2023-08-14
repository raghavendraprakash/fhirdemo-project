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
from fhir.resources import organizationaffiliation
from fhir.resources.fhirdate import FHIRDate

from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class OrganizationAffiliationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("OrganizationAffiliation", js["resourceType"])
        return organizationaffiliation.OrganizationAffiliation(js)
    
    def testOrganizationAffiliation1(self):
        inst = self.instantiate_from("orgrole-example-hie.json")
        self.assertIsNotNone(inst, "Must have instantiated a OrganizationAffiliation instance")
        self.implOrganizationAffiliation1(inst)
        
        js = inst.as_json()
        self.assertEqual("OrganizationAffiliation", js["resourceType"])
        inst2 = organizationaffiliation.OrganizationAffiliation(js)
        self.implOrganizationAffiliation1(inst2)
    
    def implOrganizationAffiliation1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.code[0].coding[0].code), force_bytes("member"))
        self.assertEqual(force_bytes(inst.code[0].coding[0].display), force_bytes("Member"))
        self.assertEqual(force_bytes(inst.code[0].coding[0].system), force_bytes("http://hl7.org/fhir/organization-role"))
        self.assertEqual(force_bytes(inst.code[0].text), force_bytes("Hospital member"))
        self.assertEqual(force_bytes(inst.id), force_bytes("orgrole2"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://example.org/www.monumentHIE.com"))
        self.assertEqual(force_bytes(inst.identifier[0].type.text), force_bytes("member hospital"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("secondary"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("hosp32"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testOrganizationAffiliation2(self):
        inst = self.instantiate_from("organizationaffiliation-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a OrganizationAffiliation instance")
        self.implOrganizationAffiliation2(inst)
        
        js = inst.as_json()
        self.assertEqual("OrganizationAffiliation", js["resourceType"])
        inst2 = organizationaffiliation.OrganizationAffiliation(js)
        self.implOrganizationAffiliation2(inst2)
    
    def implOrganizationAffiliation2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.code[0].coding[0].code), force_bytes("provider"))
        self.assertEqual(force_bytes(inst.code[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/organization-role"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.acme.org/practitioners"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("23"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(inst.period.end.date, FHIRDate("2012-03-31").date)
        self.assertEqual(inst.period.end.as_json(), "2012-03-31")
        self.assertEqual(inst.period.start.date, FHIRDate("2012-01-01").date)
        self.assertEqual(inst.period.start.as_json(), "2012-01-01")
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].code), force_bytes("408443003"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].display), force_bytes("General medical practice"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("general.practice@example.org"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testOrganizationAffiliation3(self):
        inst = self.instantiate_from("orgrole-example-services.json")
        self.assertIsNotNone(inst, "Must have instantiated a OrganizationAffiliation instance")
        self.implOrganizationAffiliation3(inst)
        
        js = inst.as_json()
        self.assertEqual("OrganizationAffiliation", js["resourceType"])
        inst2 = organizationaffiliation.OrganizationAffiliation(js)
        self.implOrganizationAffiliation3(inst2)
    
    def implOrganizationAffiliation3(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.code[0].coding[0].code), force_bytes("provider"))
        self.assertEqual(force_bytes(inst.code[0].coding[0].display), force_bytes("Provider"))
        self.assertEqual(force_bytes(inst.code[0].coding[0].system), force_bytes("http://hl7.org/fhir/organization-role"))
        self.assertTrue(inst.code[0].coding[0].userSelected)
        self.assertEqual(force_bytes(inst.code[0].text), force_bytes("Provider of rehabilitation services"))
        self.assertEqual(force_bytes(inst.id), force_bytes("orgrole1"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://example.org/www.foundingfathersmemorial.com"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("secondary"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("service002"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(inst.period.end.date, FHIRDate("2022-02-01").date)
        self.assertEqual(inst.period.end.as_json(), "2022-02-01")
        self.assertEqual(inst.period.start.date, FHIRDate("2018-02-09").date)
        self.assertEqual(inst.period.start.as_json(), "2018-02-09")
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].code), force_bytes("394602003"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].display), force_bytes("Rehabilitation - specialty"))
        self.assertEqual(force_bytes(inst.specialty[0].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.specialty[0].text), force_bytes("Rehabilitation"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("202-109-8765"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

