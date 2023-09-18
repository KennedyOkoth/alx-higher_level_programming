#!/usr/bin/python3
"""Defines unittests for base.py.
Unittest classes:
    TestBase_instantiation - line 23
    TestBase_to_json_string - line 110
    TestBase_save_to_file - line 156
    TestBase_from_json_string - line 234
    TestBase_create - line 288
    TestBase_load_from_file - line 340
    TestBase_save_to_file_csv - line 406
    TestBase_load_from_file_csv - line 484
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_id_None(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_set(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_nb_objects_increased(self):
        inital_count = Base.__nb_objects
        b = Base()
        self.assertEqual(Base.__nb_objects, inital_count + 1)

if __name__ == '__main__':
    unittest.TestCase()