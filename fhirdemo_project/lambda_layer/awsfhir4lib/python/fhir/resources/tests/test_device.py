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
from fhir.resources import device
from fhir.resources.fhirdate import FHIRDate

from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class DeviceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Device", js["resourceType"])
        return device.Device(js)
    
    def testDevice1(self):
        inst = self.instantiate_from("device-example-f001-feedingtube.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice1(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice1(inst2)
    
    def implDevice1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("f001"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http:/goodhealthhospital/identifier/devices"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f001</p><p><b>identifier</b>: 12345</p><p><b>status</b>: active</p></div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testDevice2(self):
        inst = self.instantiate_from("device-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice2(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice2(inst2)
    
    def implDevice2(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://goodcare.org/devices/id"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("345675"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: example</p><p><b>identifier</b>: 345675</p></div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

