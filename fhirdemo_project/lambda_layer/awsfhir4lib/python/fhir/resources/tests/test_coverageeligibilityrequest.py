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
from fhir.resources import coverageeligibilityrequest
from fhir.resources.fhirdate import FHIRDate

from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class CoverageEligibilityRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CoverageEligibilityRequest", js["resourceType"])
        return coverageeligibilityrequest.CoverageEligibilityRequest(js)
    
    def testCoverageEligibilityRequest1(self):
        inst = self.instantiate_from("coverageeligibilityrequest-example-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a CoverageEligibilityRequest instance")
        self.implCoverageEligibilityRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("CoverageEligibilityRequest", js["resourceType"])
        inst2 = coverageeligibilityrequest.CoverageEligibilityRequest(js)
        self.implCoverageEligibilityRequest1(inst2)
    
    def implCoverageEligibilityRequest1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.id), force_bytes("52346"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://happyvalley.com/coverageelegibilityrequest"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("52346"))
        self.assertEqual(force_bytes(inst.insurance[0].businessArrangement), force_bytes("NB8742"))
        self.assertEqual(force_bytes(inst.item[0].category.coding[0].code), force_bytes("69"))
        self.assertEqual(force_bytes(inst.item[0].category.coding[0].display), force_bytes("Maternity"))
        self.assertEqual(force_bytes(inst.item[0].category.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/ex-benefitcategory"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.priority.coding[0].code), force_bytes("normal"))
        self.assertEqual(force_bytes(inst.purpose[0]), force_bytes("validation"))
        self.assertEqual(force_bytes(inst.purpose[1]), force_bytes("benefits"))
        self.assertEqual(inst.servicedDate.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.servicedDate.as_json(), "2014-09-17")
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the CoverageEligibilityRequest</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testCoverageEligibilityRequest2(self):
        inst = self.instantiate_from("coverageeligibilityrequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CoverageEligibilityRequest instance")
        self.implCoverageEligibilityRequest2(inst)
        
        js = inst.as_json()
        self.assertEqual("CoverageEligibilityRequest", js["resourceType"])
        inst2 = coverageeligibilityrequest.CoverageEligibilityRequest(js)
        self.implCoverageEligibilityRequest2(inst2)
    
    def implCoverageEligibilityRequest2(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.id), force_bytes("52345"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://happyvalley.com/coverageelegibilityrequest"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("52345"))
        self.assertTrue(inst.insurance[0].focal)
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.priority.coding[0].code), force_bytes("normal"))
        self.assertEqual(force_bytes(inst.purpose[0]), force_bytes("validation"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the CoverageEligibilityRequest</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

