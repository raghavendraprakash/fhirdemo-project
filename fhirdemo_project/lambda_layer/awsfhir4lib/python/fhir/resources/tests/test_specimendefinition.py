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
from fhir.resources import specimendefinition
from fhir.resources.fhirdate import FHIRDate

from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class SpecimenDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SpecimenDefinition", js["resourceType"])
        return specimendefinition.SpecimenDefinition(js)
    
    def testSpecimenDefinition1(self):
        inst = self.instantiate_from("specimendefinition-example-serum-plasma.json")
        self.assertIsNotNone(inst, "Must have instantiated a SpecimenDefinition instance")
        self.implSpecimenDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("SpecimenDefinition", js["resourceType"])
        inst2 = specimendefinition.SpecimenDefinition(js)
        self.implSpecimenDefinition1(inst2)
    
    def implSpecimenDefinition1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("2364"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.patientPreparation[0].text), force_bytes("12 hour fasting"))
        self.assertEqual(force_bytes(inst.patientPreparation[1].coding[0].code), force_bytes("263678003"))
        self.assertEqual(force_bytes(inst.patientPreparation[1].coding[0].display), force_bytes("At rest"))
        self.assertEqual(force_bytes(inst.patientPreparation[1].coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.timeAspect), force_bytes("preferrably morning time"))
        self.assertEqual(force_bytes(inst.typeCollected.coding[0].code), force_bytes("122555007"))
        self.assertEqual(force_bytes(inst.typeCollected.coding[0].display), force_bytes("Venous blood specimen"))
        self.assertEqual(force_bytes(inst.typeCollected.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.typeTested[0].container.cap.coding[0].code), force_bytes("yellow"))
        self.assertEqual(force_bytes(inst.typeTested[0].container.cap.coding[0].display), force_bytes("yellow cap"))
        self.assertEqual(force_bytes(inst.typeTested[0].container.cap.coding[0].system), force_bytes("urn:iso:std:iso:6710:2017"))
        self.assertEqual(force_bytes(inst.typeTested[0].container.material.coding[0].code), force_bytes("61088005"))
        self.assertEqual(force_bytes(inst.typeTested[0].container.material.coding[0].display), force_bytes("plastic"))
        self.assertEqual(force_bytes(inst.typeTested[0].container.material.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.typeTested[0].container.minimumVolumeQuantity.code), force_bytes("mL"))
        self.assertEqual(force_bytes(inst.typeTested[0].container.minimumVolumeQuantity.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.typeTested[0].container.minimumVolumeQuantity.unit), force_bytes("ml"))
        self.assertEqual(inst.typeTested[0].container.minimumVolumeQuantity.value, 2)
        self.assertEqual(force_bytes(inst.typeTested[0].container.type.coding[0].code), force_bytes("702281005"))
        self.assertEqual(force_bytes(inst.typeTested[0].container.type.coding[0].display), force_bytes("Evacuated blood collection tube, thrombin/clot activator/gel separator"))
        self.assertEqual(force_bytes(inst.typeTested[0].container.type.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.typeTested[0].handling[0].maxDuration.code), force_bytes("min"))
        self.assertEqual(force_bytes(inst.typeTested[0].handling[0].maxDuration.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.typeTested[0].handling[0].maxDuration.unit), force_bytes("minute"))
        self.assertEqual(inst.typeTested[0].handling[0].maxDuration.value, 60)
        self.assertEqual(force_bytes(inst.typeTested[0].handling[0].temperatureQualifier.text), force_bytes("Ambient temperature"))
        self.assertEqual(force_bytes(inst.typeTested[0].handling[0].temperatureRange.high.code), force_bytes("Cel"))
        self.assertEqual(force_bytes(inst.typeTested[0].handling[0].temperatureRange.high.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.typeTested[0].handling[0].temperatureRange.high.unit), force_bytes("°C"))
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.high.value, 25)
        self.assertEqual(force_bytes(inst.typeTested[0].handling[0].temperatureRange.low.code), force_bytes("Cel"))
        self.assertEqual(force_bytes(inst.typeTested[0].handling[0].temperatureRange.low.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.typeTested[0].handling[0].temperatureRange.low.unit), force_bytes("°C"))
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.low.value, 15)
        self.assertEqual(force_bytes(inst.typeTested[0].handling[1].maxDuration.code), force_bytes("h"))
        self.assertEqual(force_bytes(inst.typeTested[0].handling[1].maxDuration.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.typeTested[0].handling[1].maxDuration.unit), force_bytes("hour"))
        self.assertEqual(inst.typeTested[0].handling[1].maxDuration.value, 8)
        self.assertEqual(force_bytes(inst.typeTested[0].handling[1].temperatureQualifier.text), force_bytes("Refrigerated temperature"))
        self.assertEqual(force_bytes(inst.typeTested[0].handling[1].temperatureRange.high.code), force_bytes("Cel"))
        self.assertEqual(force_bytes(inst.typeTested[0].handling[1].temperatureRange.high.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.typeTested[0].handling[1].temperatureRange.high.unit), force_bytes("°C"))
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.high.value, 8)
        self.assertEqual(force_bytes(inst.typeTested[0].handling[1].temperatureRange.low.code), force_bytes("Cel"))
        self.assertEqual(force_bytes(inst.typeTested[0].handling[1].temperatureRange.low.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.typeTested[0].handling[1].temperatureRange.low.unit), force_bytes("°C"))
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.low.value, 2)
        self.assertEqual(force_bytes(inst.typeTested[0].preference), force_bytes("preferred"))
        self.assertEqual(force_bytes(inst.typeTested[0].type.coding[0].code), force_bytes("119364003"))
        self.assertEqual(force_bytes(inst.typeTested[0].type.coding[0].display), force_bytes("Serum specimen"))
        self.assertEqual(force_bytes(inst.typeTested[0].type.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.typeTested[1].container.cap.coding[0].code), force_bytes("green"))
        self.assertEqual(force_bytes(inst.typeTested[1].container.cap.coding[0].display), force_bytes("green cap"))
        self.assertEqual(force_bytes(inst.typeTested[1].container.cap.coding[0].system), force_bytes("urn:iso:std:iso:6710:2017"))
        self.assertEqual(force_bytes(inst.typeTested[1].container.material.coding[0].code), force_bytes("32039001"))
        self.assertEqual(force_bytes(inst.typeTested[1].container.material.coding[0].display), force_bytes("glass"))
        self.assertEqual(force_bytes(inst.typeTested[1].container.material.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.typeTested[1].container.minimumVolumeQuantity.code), force_bytes("mL"))
        self.assertEqual(force_bytes(inst.typeTested[1].container.minimumVolumeQuantity.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.typeTested[1].container.minimumVolumeQuantity.unit), force_bytes("ml"))
        self.assertEqual(inst.typeTested[1].container.minimumVolumeQuantity.value, 2)
        self.assertEqual(force_bytes(inst.typeTested[1].container.type.coding[0].code), force_bytes("767390000"))
        self.assertEqual(force_bytes(inst.typeTested[1].container.type.coding[0].display), force_bytes("Evacuated blood collection tube with heparin lithium and gel separator"))
        self.assertEqual(force_bytes(inst.typeTested[1].container.type.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.typeTested[1].handling[0].maxDuration.code), force_bytes("min"))
        self.assertEqual(force_bytes(inst.typeTested[1].handling[0].maxDuration.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.typeTested[1].handling[0].maxDuration.unit), force_bytes("minute"))
        self.assertEqual(inst.typeTested[1].handling[0].maxDuration.value, 60)
        self.assertEqual(force_bytes(inst.typeTested[1].handling[0].temperatureQualifier.text), force_bytes("Ambient temperature"))
        self.assertEqual(force_bytes(inst.typeTested[1].handling[0].temperatureRange.high.code), force_bytes("Cel"))
        self.assertEqual(force_bytes(inst.typeTested[1].handling[0].temperatureRange.high.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.typeTested[1].handling[0].temperatureRange.high.unit), force_bytes("°C"))
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.high.value, 25)
        self.assertEqual(force_bytes(inst.typeTested[1].handling[0].temperatureRange.low.code), force_bytes("Cel"))
        self.assertEqual(force_bytes(inst.typeTested[1].handling[0].temperatureRange.low.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.typeTested[1].handling[0].temperatureRange.low.unit), force_bytes("°C"))
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.low.value, 15)
        self.assertEqual(force_bytes(inst.typeTested[1].handling[1].maxDuration.code), force_bytes("h"))
        self.assertEqual(force_bytes(inst.typeTested[1].handling[1].maxDuration.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.typeTested[1].handling[1].maxDuration.unit), force_bytes("hour"))
        self.assertEqual(inst.typeTested[1].handling[1].maxDuration.value, 8)
        self.assertEqual(force_bytes(inst.typeTested[1].handling[1].temperatureQualifier.text), force_bytes("Refrigerated temperature"))
        self.assertEqual(force_bytes(inst.typeTested[1].handling[1].temperatureRange.high.code), force_bytes("Cel"))
        self.assertEqual(force_bytes(inst.typeTested[1].handling[1].temperatureRange.high.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.typeTested[1].handling[1].temperatureRange.high.unit), force_bytes("°C"))
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.high.value, 8)
        self.assertEqual(force_bytes(inst.typeTested[1].handling[1].temperatureRange.low.code), force_bytes("Cel"))
        self.assertEqual(force_bytes(inst.typeTested[1].handling[1].temperatureRange.low.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.typeTested[1].handling[1].temperatureRange.low.unit), force_bytes("°C"))
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.low.value, 2)
        self.assertEqual(force_bytes(inst.typeTested[1].preference), force_bytes("alternate"))
        self.assertEqual(force_bytes(inst.typeTested[1].rejectionCriterion[0].coding[0].code), force_bytes("insufficient"))
        self.assertEqual(force_bytes(inst.typeTested[1].rejectionCriterion[0].coding[0].display), force_bytes("insufficient specimen volume"))
        self.assertEqual(force_bytes(inst.typeTested[1].rejectionCriterion[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/rejection-criteria"))
        self.assertEqual(force_bytes(inst.typeTested[1].rejectionCriterion[1].coding[0].code), force_bytes("hemolized"))
        self.assertEqual(force_bytes(inst.typeTested[1].rejectionCriterion[1].coding[0].display), force_bytes("hemolized specimen"))
        self.assertEqual(force_bytes(inst.typeTested[1].rejectionCriterion[1].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/rejection-criteria"))
        self.assertEqual(force_bytes(inst.typeTested[1].type.coding[0].code), force_bytes("119361006"))
        self.assertEqual(force_bytes(inst.typeTested[1].type.coding[0].display), force_bytes("Plasma specimen"))
        self.assertEqual(force_bytes(inst.typeTested[1].type.coding[0].system), force_bytes("http://snomed.info/sct"))

