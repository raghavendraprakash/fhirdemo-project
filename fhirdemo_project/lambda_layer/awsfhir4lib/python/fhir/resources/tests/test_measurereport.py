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
from fhir.resources import measurereport
from fhir.resources.fhirdate import FHIRDate

from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class MeasureReportTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MeasureReport", js["resourceType"])
        return measurereport.MeasureReport(js)
    
    def testMeasureReport1(self):
        inst = self.instantiate_from("measurereport-cms146-cat3-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MeasureReport instance")
        self.implMeasureReport1(inst)
        
        js = inst.as_json()
        self.assertEqual("MeasureReport", js["resourceType"])
        inst2 = measurereport.MeasureReport(js)
        self.implMeasureReport1(inst2)
    
    def implMeasureReport1(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("reporter"))
        self.assertEqual(inst.date.date, FHIRDate("2014-04-01").date)
        self.assertEqual(inst.date.as_json(), "2014-04-01")
        self.assertEqual(force_bytes(inst.group[0].id), force_bytes("CMS146-group-1"))
        self.assertEqual(force_bytes(inst.group[0].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].population[0].count, 500)
        self.assertEqual(force_bytes(inst.group[0].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].population[1].count, 200)
        self.assertEqual(force_bytes(inst.group[0].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].population[2].count, 500)
        self.assertEqual(force_bytes(inst.group[0].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].population[3].count, 100)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].code[0].text), force_bytes("stratifier-ages-up-to-9"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[0].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[0].population[0].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[0].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[0].population[1].count, 100)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[0].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[0].population[2].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[0].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[0].population[3].count, 50)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[0].value.text), force_bytes("true"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[1].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[1].population[0].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[1].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[1].population[1].count, 100)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[1].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[1].population[2].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[1].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[1].population[3].count, 50)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[1].value.text), force_bytes("false"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].code[0].text), force_bytes("stratifier-ages-10-plus"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[0].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[0].population[0].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[0].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[0].population[1].count, 100)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[0].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[0].population[2].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[0].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[0].population[3].count, 50)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[0].value.text), force_bytes("true"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[1].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[1].population[0].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[1].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[1].population[1].count, 100)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[1].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[1].population[2].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[1].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[1].population[3].count, 50)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[1].value.text), force_bytes("false"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].code[0].text), force_bytes("stratifier-gender"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[0].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[0].population[0].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[0].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[0].population[1].count, 100)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[0].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[0].population[2].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[0].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[0].population[3].count, 50)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[0].value.text), force_bytes("male"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[1].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[1].population[0].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[1].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[1].population[1].count, 100)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[1].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[1].population[2].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[1].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[1].population[3].count, 50)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[1].value.text), force_bytes("female"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[2].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[2].population[0].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[2].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[2].population[1].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[2].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[2].population[2].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[2].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[2].population[3].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[2].value.text), force_bytes("other"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[3].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[3].population[0].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[3].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[3].population[1].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[3].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[3].population[2].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[3].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[3].population[3].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[3].value.text), force_bytes("unknown"))
        self.assertEqual(force_bytes(inst.id), force_bytes("measurereport-cms146-cat3-example"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("measurereport-cms146-cat3-example-2017-03-13"))
        self.assertEqual(force_bytes(inst.measure), force_bytes("Measure/CMS146"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(inst.period.end.date, FHIRDate("2014-03-31").date)
        self.assertEqual(inst.period.end.as_json(), "2014-03-31")
        self.assertEqual(inst.period.start.date, FHIRDate("2014-01-01").date)
        self.assertEqual(inst.period.start.as_json(), "2014-01-01")
        self.assertEqual(force_bytes(inst.status), force_bytes("complete"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("summary"))
    
    def testMeasureReport2(self):
        inst = self.instantiate_from("measurereport-cms146-cat2-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MeasureReport instance")
        self.implMeasureReport2(inst)
        
        js = inst.as_json()
        self.assertEqual("MeasureReport", js["resourceType"])
        inst2 = measurereport.MeasureReport(js)
        self.implMeasureReport2(inst2)
    
    def implMeasureReport2(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("reporter"))
        self.assertEqual(inst.date.date, FHIRDate("2014-04-01").date)
        self.assertEqual(inst.date.as_json(), "2014-04-01")
        self.assertEqual(force_bytes(inst.group[0].id), force_bytes("CMS146-group-1"))
        self.assertEqual(force_bytes(inst.group[0].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].population[0].count, 500)
        self.assertEqual(force_bytes(inst.group[0].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].population[1].count, 200)
        self.assertEqual(force_bytes(inst.group[0].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].population[2].count, 500)
        self.assertEqual(force_bytes(inst.group[0].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].population[3].count, 100)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].code[0].text), force_bytes("stratifier-ages-up-to-9"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[0].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[0].population[0].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[0].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[0].population[1].count, 100)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[0].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[0].population[2].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[0].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[0].population[3].count, 50)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[0].value.text), force_bytes("true"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[1].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[1].population[0].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[1].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[1].population[1].count, 100)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[1].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[1].population[2].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[1].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[1].population[3].count, 50)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[1].value.text), force_bytes("false"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].code[0].text), force_bytes("stratifier-ages-10-plus"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[0].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[0].population[0].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[0].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[0].population[1].count, 100)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[0].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[0].population[2].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[0].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[0].population[3].count, 50)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[0].value.text), force_bytes("true"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[1].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[1].population[0].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[1].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[1].population[1].count, 100)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[1].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[1].population[2].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[1].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[1].population[3].count, 50)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[1].value.text), force_bytes("false"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].code[0].text), force_bytes("stratifier-gender"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[0].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[0].population[0].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[0].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[0].population[1].count, 100)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[0].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[0].population[2].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[0].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[0].population[3].count, 50)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[0].value.text), force_bytes("male"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[1].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[1].population[0].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[1].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[1].population[1].count, 100)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[1].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[1].population[2].count, 250)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[1].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[1].population[3].count, 50)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[1].value.text), force_bytes("female"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[2].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[2].population[0].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[2].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[2].population[1].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[2].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[2].population[2].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[2].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[2].population[3].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[2].value.text), force_bytes("other"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[3].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[3].population[0].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[3].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[3].population[1].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[3].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[3].population[2].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[3].population[3].code.coding[0].code), force_bytes("denominator-exclusions"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[3].population[3].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[3].value.text), force_bytes("unknown"))
        self.assertEqual(force_bytes(inst.id), force_bytes("measurereport-cms146-cat2-example"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("measurereport-cms146-cat2-example-2017-03-13"))
        self.assertEqual(force_bytes(inst.measure), force_bytes("Measure/CMS146"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(inst.period.end.date, FHIRDate("2014-03-31").date)
        self.assertEqual(inst.period.end.as_json(), "2014-03-31")
        self.assertEqual(inst.period.start.date, FHIRDate("2014-01-01").date)
        self.assertEqual(inst.period.start.as_json(), "2014-01-01")
        self.assertEqual(force_bytes(inst.status), force_bytes("complete"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("subject-list"))
    
    def testMeasureReport3(self):
        inst = self.instantiate_from("measurereport-cms146-cat1-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MeasureReport instance")
        self.implMeasureReport3(inst)
        
        js = inst.as_json()
        self.assertEqual("MeasureReport", js["resourceType"])
        inst2 = measurereport.MeasureReport(js)
        self.implMeasureReport3(inst2)
    
    def implMeasureReport3(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("reporter"))
        self.assertEqual(inst.date.date, FHIRDate("2014-04-01").date)
        self.assertEqual(inst.date.as_json(), "2014-04-01")
        self.assertEqual(force_bytes(inst.group[0].id), force_bytes("CMS146-group-1"))
        self.assertEqual(force_bytes(inst.group[0].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].population[0].count, 1)
        self.assertEqual(force_bytes(inst.group[0].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].population[1].count, 1)
        self.assertEqual(force_bytes(inst.group[0].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].population[2].count, 1)
        self.assertEqual(force_bytes(inst.group[0].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].population[3].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].code[0].text), force_bytes("stratifier-ages-up-to-9"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[0].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[0].population[0].count, 1)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[0].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[0].population[1].count, 1)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[0].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[0].population[2].count, 1)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[0].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[0].population[3].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[0].value.text), force_bytes("true"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[1].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[1].population[0].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[1].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[1].population[1].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[1].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[1].population[2].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[1].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[0].stratum[1].population[3].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].stratum[1].value.text), force_bytes("false"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].code[0].text), force_bytes("stratifier-ages-10-plus"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[0].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[0].population[0].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[0].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[0].population[1].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[0].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[0].population[2].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[0].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[0].population[3].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[0].value.text), force_bytes("true"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[1].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[1].population[0].count, 1)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[1].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[1].population[1].count, 1)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[1].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[1].population[2].count, 1)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[1].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[1].stratum[1].population[3].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].stratum[1].value.text), force_bytes("false"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].code[0].text), force_bytes("stratifier-gender"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[0].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[0].population[0].count, 1)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[0].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[0].population[1].count, 1)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[0].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[0].population[2].count, 1)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[0].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[0].population[3].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[0].value.text), force_bytes("male"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[1].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[1].population[0].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[1].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[1].population[1].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[1].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[1].population[2].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[1].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[1].population[3].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[1].value.text), force_bytes("female"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[2].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[2].population[0].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[2].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[2].population[1].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[2].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[2].population[2].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[2].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[2].population[3].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[2].value.text), force_bytes("other"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[3].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[3].population[0].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[3].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[3].population[1].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[3].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[3].population[2].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[3].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(inst.group[0].stratifier[2].stratum[3].population[3].count, 0)
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].stratum[3].value.text), force_bytes("unknown"))
        self.assertEqual(force_bytes(inst.id), force_bytes("measurereport-cms146-cat1-example"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("measurereport-cms146-cat1-example-2017-03-13"))
        self.assertEqual(force_bytes(inst.measure), force_bytes("Measure/CMS146"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(inst.period.end.date, FHIRDate("2014-03-31").date)
        self.assertEqual(inst.period.end.as_json(), "2014-03-31")
        self.assertEqual(inst.period.start.date, FHIRDate("2014-01-01").date)
        self.assertEqual(inst.period.start.as_json(), "2014-01-01")
        self.assertEqual(force_bytes(inst.status), force_bytes("complete"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("individual"))

