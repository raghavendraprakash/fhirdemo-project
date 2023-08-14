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
from fhir.resources import medicinalproductcontraindication
from fhir.resources.fhirdate import FHIRDate

from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class MedicinalProductContraindicationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductContraindication", js["resourceType"])
        return medicinalproductcontraindication.MedicinalProductContraindication(js)
    
    def testMedicinalProductContraindication1(self):
        inst = self.instantiate_from("medicinalproductcontraindication-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicinalProductContraindication instance")
        self.implMedicinalProductContraindication1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicinalProductContraindication", js["resourceType"])
        inst2 = medicinalproductcontraindication.MedicinalProductContraindication(js)
        self.implMedicinalProductContraindication1(inst2)
    
    def implMedicinalProductContraindication1(self, inst):
        self.assertEqual(force_bytes(inst.comorbidity[0].coding[0].code), force_bytes("Hepaticdisease"))
        self.assertEqual(force_bytes(inst.comorbidity[0].coding[0].system), force_bytes("http://ema.europa.eu/example/comorbidity"))
        self.assertEqual(force_bytes(inst.disease.coding[0].code), force_bytes("Coagulopathiesandbleedingdiatheses(exclthrombocytopenic)"))
        self.assertEqual(force_bytes(inst.disease.coding[0].system), force_bytes("http://ema.europa.eu/example/contraindicationsasdisease-symptom-procedure"))
        self.assertEqual(force_bytes(inst.disease.text), force_bytes("Hepatic disease associated with coagulopathy and clinically relevant bleeding risk"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

