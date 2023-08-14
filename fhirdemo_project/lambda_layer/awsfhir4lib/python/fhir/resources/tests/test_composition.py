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
from fhir.resources import composition
from fhir.resources.fhirdate import FHIRDate

from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class CompositionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Composition", js["resourceType"])
        return composition.Composition(js)
    
    def testComposition1(self):
        inst = self.instantiate_from("composition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Composition instance")
        self.implComposition1(inst)
        
        js = inst.as_json()
        self.assertEqual("Composition", js["resourceType"])
        inst2 = composition.Composition(js)
        self.implComposition1(inst2)
    
    def implComposition1(self, inst):
        self.assertEqual(force_bytes(inst.attester[0].mode), force_bytes("legal"))
        self.assertEqual(inst.attester[0].time.date, FHIRDate("2012-01-04T09:10:14Z").date)
        self.assertEqual(inst.attester[0].time.as_json(), "2012-01-04T09:10:14Z")
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("LP173421-1"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("Report"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.confidentiality), force_bytes("N"))
        self.assertEqual(inst.date.date, FHIRDate("2012-01-04T09:10:14Z").date)
        self.assertEqual(inst.date.as_json(), "2012-01-04T09:10:14Z")
        self.assertEqual(force_bytes(inst.event[0].code[0].coding[0].code), force_bytes("HEALTHREC"))
        self.assertEqual(force_bytes(inst.event[0].code[0].coding[0].display), force_bytes("health record"))
        self.assertEqual(force_bytes(inst.event[0].code[0].coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActCode"))
        self.assertEqual(inst.event[0].period.end.date, FHIRDate("2012-11-12").date)
        self.assertEqual(inst.event[0].period.end.as_json(), "2012-11-12")
        self.assertEqual(inst.event[0].period.start.date, FHIRDate("2010-07-18").date)
        self.assertEqual(inst.event[0].period.start.as_json(), "2010-07-18")
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier.system), force_bytes("http://healthintersections.com.au/test"))
        self.assertEqual(force_bytes(inst.identifier.value), force_bytes("1"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.relatesTo[0].code), force_bytes("replaces"))
        self.assertEqual(force_bytes(inst.relatesTo[1].code), force_bytes("appends"))
        self.assertEqual(force_bytes(inst.relatesTo[1].targetIdentifier.system), force_bytes("http://example.org/fhir/NamingSystem/document-ids"))
        self.assertEqual(force_bytes(inst.relatesTo[1].targetIdentifier.value), force_bytes("ABC123"))
        self.assertEqual(force_bytes(inst.section[0].code.coding[0].code), force_bytes("11348-0"))
        self.assertEqual(force_bytes(inst.section[0].code.coding[0].display), force_bytes("History of past illness Narrative"))
        self.assertEqual(force_bytes(inst.section[0].code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.section[0].mode), force_bytes("snapshot"))
        self.assertEqual(force_bytes(inst.section[0].orderedBy.coding[0].code), force_bytes("event-date"))
        self.assertEqual(force_bytes(inst.section[0].orderedBy.coding[0].display), force_bytes("Sorted by Event Date"))
        self.assertEqual(force_bytes(inst.section[0].orderedBy.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/list-order"))
        self.assertEqual(force_bytes(inst.section[0].text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.section[0].title), force_bytes("History of present illness"))
        self.assertEqual(force_bytes(inst.section[1].code.coding[0].code), force_bytes("10157-6"))
        self.assertEqual(force_bytes(inst.section[1].code.coding[0].display), force_bytes("History of family member diseases Narrative"))
        self.assertEqual(force_bytes(inst.section[1].code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.section[1].emptyReason.coding[0].code), force_bytes("withheld"))
        self.assertEqual(force_bytes(inst.section[1].emptyReason.coding[0].display), force_bytes("Information Withheld"))
        self.assertEqual(force_bytes(inst.section[1].emptyReason.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/list-empty-reason"))
        self.assertEqual(force_bytes(inst.section[1].mode), force_bytes("snapshot"))
        self.assertEqual(force_bytes(inst.section[1].text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.section[1].title), force_bytes("History of family member diseases"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Consultation Note"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("11488-4"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("Consult note"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://loinc.org"))
    
    def testComposition2(self):
        inst = self.instantiate_from("composition-example-mixed.json")
        self.assertIsNotNone(inst, "Must have instantiated a Composition instance")
        self.implComposition2(inst)
        
        js = inst.as_json()
        self.assertEqual("Composition", js["resourceType"])
        inst2 = composition.Composition(js)
        self.implComposition2(inst2)
    
    def implComposition2(self, inst):
        self.assertEqual(force_bytes(inst.attester[0].mode), force_bytes("legal"))
        self.assertEqual(inst.attester[0].time.date, FHIRDate("2012-01-04T09:10:14Z").date)
        self.assertEqual(inst.attester[0].time.as_json(), "2012-01-04T09:10:14Z")
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("LP173421-1"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("Report"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.confidentiality), force_bytes("N"))
        self.assertEqual(inst.date.date, FHIRDate("2018-10-30T16:56:04+11:00").date)
        self.assertEqual(inst.date.as_json(), "2018-10-30T16:56:04+11:00")
        self.assertEqual(force_bytes(inst.id), force_bytes("example-mixed"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.section[0].code.coding[0].code), force_bytes("newborn"))
        self.assertEqual(force_bytes(inst.section[0].code.coding[0].display), force_bytes("New Born Details"))
        self.assertEqual(force_bytes(inst.section[0].code.coding[0].system), force_bytes("http://acme.org/codes/SectionType"))
        self.assertEqual(force_bytes(inst.section[0].text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.section[0].title), force_bytes("Child's Details"))
        self.assertEqual(force_bytes(inst.section[1].code.coding[0].code), force_bytes("mother"))
        self.assertEqual(force_bytes(inst.section[1].code.coding[0].display), force_bytes("Mother's Details"))
        self.assertEqual(force_bytes(inst.section[1].code.coding[0].system), force_bytes("http://acme.org/codes/SectionType"))
        self.assertEqual(force_bytes(inst.section[1].text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.section[1].title), force_bytes("Mpther's Details"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Discharge Summary (Neonatal Service)"))
        self.assertEqual(force_bytes(inst.type.coding[0].code), force_bytes("78418-1"))
        self.assertEqual(force_bytes(inst.type.coding[0].display), force_bytes("Neonatal perinatal medicine Discharge summary"))
        self.assertEqual(force_bytes(inst.type.coding[0].system), force_bytes("http://loinc.org"))

