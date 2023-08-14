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
from fhir.resources import visionprescription
from fhir.resources.fhirdate import FHIRDate

from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class VisionPrescriptionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("VisionPrescription", js["resourceType"])
        return visionprescription.VisionPrescription(js)
    
    def testVisionPrescription1(self):
        inst = self.instantiate_from("visionprescription-example-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a VisionPrescription instance")
        self.implVisionPrescription1(inst)
        
        js = inst.as_json()
        self.assertEqual("VisionPrescription", js["resourceType"])
        inst2 = visionprescription.VisionPrescription(js)
        self.implVisionPrescription1(inst2)
    
    def implVisionPrescription1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-06-15").date)
        self.assertEqual(inst.created.as_json(), "2014-06-15")
        self.assertEqual(inst.dateWritten.date, FHIRDate("2014-06-15").date)
        self.assertEqual(inst.dateWritten.as_json(), "2014-06-15")
        self.assertEqual(force_bytes(inst.id), force_bytes("33124"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.happysight.com/prescription"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("15014"))
        self.assertEqual(inst.lensSpecification[0].add, 1.75)
        self.assertEqual(inst.lensSpecification[0].axis, 160)
        self.assertEqual(inst.lensSpecification[0].backCurve, 8.7)
        self.assertEqual(force_bytes(inst.lensSpecification[0].brand), force_bytes("OphthaGuard"))
        self.assertEqual(force_bytes(inst.lensSpecification[0].color), force_bytes("green"))
        self.assertEqual(inst.lensSpecification[0].cylinder, -2.25)
        self.assertEqual(inst.lensSpecification[0].diameter, 14.0)
        self.assertEqual(force_bytes(inst.lensSpecification[0].duration.code), force_bytes("month"))
        self.assertEqual(force_bytes(inst.lensSpecification[0].duration.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.lensSpecification[0].duration.unit), force_bytes("month"))
        self.assertEqual(inst.lensSpecification[0].duration.value, 1)
        self.assertEqual(force_bytes(inst.lensSpecification[0].eye), force_bytes("right"))
        self.assertEqual(force_bytes(inst.lensSpecification[0].note[0].text), force_bytes("Shade treatment for extreme light sensitivity"))
        self.assertEqual(inst.lensSpecification[0].power, -2.75)
        self.assertEqual(force_bytes(inst.lensSpecification[0].product.coding[0].code), force_bytes("contact"))
        self.assertEqual(force_bytes(inst.lensSpecification[0].product.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct"))
        self.assertEqual(inst.lensSpecification[1].add, 1.75)
        self.assertEqual(inst.lensSpecification[1].axis, 160)
        self.assertEqual(inst.lensSpecification[1].backCurve, 8.7)
        self.assertEqual(force_bytes(inst.lensSpecification[1].brand), force_bytes("OphthaGuard"))
        self.assertEqual(force_bytes(inst.lensSpecification[1].color), force_bytes("green"))
        self.assertEqual(inst.lensSpecification[1].cylinder, -3.5)
        self.assertEqual(inst.lensSpecification[1].diameter, 14.0)
        self.assertEqual(force_bytes(inst.lensSpecification[1].duration.code), force_bytes("month"))
        self.assertEqual(force_bytes(inst.lensSpecification[1].duration.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.lensSpecification[1].duration.unit), force_bytes("month"))
        self.assertEqual(inst.lensSpecification[1].duration.value, 1)
        self.assertEqual(force_bytes(inst.lensSpecification[1].eye), force_bytes("left"))
        self.assertEqual(force_bytes(inst.lensSpecification[1].note[0].text), force_bytes("Shade treatment for extreme light sensitivity"))
        self.assertEqual(inst.lensSpecification[1].power, -2.75)
        self.assertEqual(force_bytes(inst.lensSpecification[1].product.coding[0].code), force_bytes("contact"))
        self.assertEqual(force_bytes(inst.lensSpecification[1].product.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">Sample Contract Lens prescription</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testVisionPrescription2(self):
        inst = self.instantiate_from("visionprescription-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a VisionPrescription instance")
        self.implVisionPrescription2(inst)
        
        js = inst.as_json()
        self.assertEqual("VisionPrescription", js["resourceType"])
        inst2 = visionprescription.VisionPrescription(js)
        self.implVisionPrescription2(inst2)
    
    def implVisionPrescription2(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-06-15").date)
        self.assertEqual(inst.created.as_json(), "2014-06-15")
        self.assertEqual(inst.dateWritten.date, FHIRDate("2014-06-15").date)
        self.assertEqual(inst.dateWritten.as_json(), "2014-06-15")
        self.assertEqual(force_bytes(inst.id), force_bytes("33123"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.happysight.com/prescription"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("15013"))
        self.assertEqual(inst.lensSpecification[0].add, 2.0)
        self.assertEqual(force_bytes(inst.lensSpecification[0].eye), force_bytes("right"))
        self.assertEqual(inst.lensSpecification[0].prism[0].amount, 0.5)
        self.assertEqual(force_bytes(inst.lensSpecification[0].prism[0].base), force_bytes("down"))
        self.assertEqual(force_bytes(inst.lensSpecification[0].product.coding[0].code), force_bytes("lens"))
        self.assertEqual(force_bytes(inst.lensSpecification[0].product.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct"))
        self.assertEqual(inst.lensSpecification[0].sphere, -2.0)
        self.assertEqual(inst.lensSpecification[1].add, 2.0)
        self.assertEqual(inst.lensSpecification[1].axis, 180)
        self.assertEqual(inst.lensSpecification[1].cylinder, -0.5)
        self.assertEqual(force_bytes(inst.lensSpecification[1].eye), force_bytes("left"))
        self.assertEqual(inst.lensSpecification[1].prism[0].amount, 0.5)
        self.assertEqual(force_bytes(inst.lensSpecification[1].prism[0].base), force_bytes("up"))
        self.assertEqual(force_bytes(inst.lensSpecification[1].product.coding[0].code), force_bytes("lens"))
        self.assertEqual(force_bytes(inst.lensSpecification[1].product.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct"))
        self.assertEqual(inst.lensSpecification[1].sphere, -1.0)
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

