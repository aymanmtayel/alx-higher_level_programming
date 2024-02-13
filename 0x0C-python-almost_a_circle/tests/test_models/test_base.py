#!/usr/bin/python3
"""Unittest for base class module"""

import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """unittest class initialization"""

    def test_no_id(self):
        test1 = Base()
        test2 = Base()
        test3 = Base()
        self.assertEqual(test1.id, 1)
        self.assertEqual(test2.id, 2)
        self.assertEqual(test3.id, 3)

    def test_ass_id(self):
        test1 = Base(89)
        self.assertEqual(test1.id, 89)

    def test_None_json_string(self):
        test1 = Base.to_json_string(None)
        self.assertEqual(test1, "[]")

    def test_json_string_normal(self):
        test1 = Base.to_json_string([{"id": 12}])
        self.assertEqual(test1, '[{"id": 12}]')

    def test_from_json_None(self):
        test1 = Base.from_json_string(None)
        self.assertEqual(test1, "[]")

    def test_from_json_string(self):
        inputed = [{"id": 89}]
        saved = Base.to_json_string(inputed)
        test1= Base.from_json_string(saved)
        self.assertEqual(list, type(test1))
