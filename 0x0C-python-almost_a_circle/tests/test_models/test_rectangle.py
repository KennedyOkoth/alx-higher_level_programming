#!/usr/bin/python3
"""Defines unittests for models/rectangle.py.
Unittest classes:
    TestRectangle_instantiation - line 25
    TestRectangle_width - line 114
    TestRectangle_height - line 190
    TestRectangle_x - line 262
    TestRectangle_y - line 334
    TestRectangle_order_of_initialization - line 402
    TestRectangle_area - line 430
    TestRectangle_update_args - line 538
    TestRectangle_update_kwargs - line 676
    TestRectangle_to_dictionary - line 788
"""
import io
import sys
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_inheritance(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_attributes(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        
        # Check private attributes
        self.assertEqual(r1._Rectangle__width, 10)
        self.assertEqual(r1._Rectangle__height, 20)

    def test_setters(self):
        r = Rectangle(10, 20)
        r.width = 30
        r.height = 40
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 40)

    def test_init(self):
        r2 = Rectangle(10, 20, 5, 7, 100)
        self.assertEqual(r2.id, 100)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 20)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r2.y, 7)


    def test_width_typeerror(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle("invalid", 2)
        self.assertTrue("width must be an integer" in str(context.exception))

    def test_width_valueerror(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(-10, 2)
        self.assertTrue("width must be > 0" in str(context.exception))
    
    def test_height_typeerror(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, "invalid")
        self.assertTrue("height must be an integer" in str(context.exception))

    def test_height_valueerror(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, -2)
        self.assertTrue("height must be > 0" in str(context.exception))

    # Tests for x and y validations

if __name__ == '__main__':
    unittest.main()