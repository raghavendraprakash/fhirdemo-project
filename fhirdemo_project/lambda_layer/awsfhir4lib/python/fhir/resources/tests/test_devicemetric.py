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
from fhir.resources import devicemetric
from fhir.resources.fhirdate import FHIRDate

from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class DeviceMetricTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DeviceMetric", js["resourceType"])
        return devicemetric.DeviceMetric(js)
    
    def testDeviceMetric1(self):
        inst = self.instantiate_from("devicemetric-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceMetric instance")
        self.implDeviceMetric1(inst)
        
        js = inst.as_json()
        self.assertEqual("DeviceMetric", js["resourceType"])
        inst2 = devicemetric.DeviceMetric(js)
        self.implDeviceMetric1(inst2)
    
    def implDeviceMetric1(self, inst):
        self.assertEqual(force_bytes(inst.calibration[0].state), force_bytes("calibrated"))
        self.assertEqual(inst.calibration[0].time.date, FHIRDate("2016-12-28T09:03:04-05:00").date)
        self.assertEqual(inst.calibration[0].time.as_json(), "2016-12-28T09:03:04-05:00")
        self.assertEqual(force_bytes(inst.calibration[0].type), force_bytes("two-point"))
        self.assertEqual(force_bytes(inst.category), force_bytes("measurement"))
        self.assertEqual(force_bytes(inst.color), force_bytes("blue"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://goodcare.org/devicemetric/id"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("345675"))
        self.assertEqual(inst.measurementPeriod.repeat.frequency, 1)
        self.assertEqual(inst.measurementPeriod.repeat.period, 1)
        self.assertEqual(force_bytes(inst.measurementPeriod.repeat.periodUnit), force_bytes("s"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.operationalStatus), force_bytes("on"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("150456"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("MDC_PULS_OXIM_SAT_O2"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("urn:iso:std:iso:11073:10101"))
        self.assertEqual(force_bytes(inst.unit.coding[0].code), force_bytes("262688"))
        self.assertEqual(force_bytes(inst.unit.coding[0].display), force_bytes("MDC_DIM_PERCENT"))
        self.assertEqual(force_bytes(inst.unit.coding[0].system), force_bytes("urn:iso:std:iso:11073:10101"))

