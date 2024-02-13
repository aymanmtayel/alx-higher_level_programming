#!/usr/bin/python3
"""Unittest for rectangle module"""


import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle



class TestRectangle(unittest.TestCase):
    """unittest for rectangle class"""

    def test_rectangle_exist(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)

    def test_r_x_only(self):
        r1 = Rectangle(1, 2, 3)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 0)

    def test_r_x_y(self):
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_r_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

    def test_r_height_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

    def test_r_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")

    def test_r_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_r_all_args(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 5)

    def test_r_neg_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_r_neg_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_r_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_r_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_r_neg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)

    def test_r_neg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_r_area_with_all_args(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.area(), 2)

class TestRectangle_display(unittest.TestCase):
    """unittest for testing __str__ and display of the rectangle
    and all the information to be printed out"""
    @staticmethod
    def printed(obj, method_name):
        """get the printed string in the stdout

        Args:
            rec: the rectangle which information to be printed
            method: the method called
        
        Returns: the printed string"""
        import io
        import sys
        output = io.StringIO()
        sys.stdout = output
        if method_name == "display":
            getattr(obj, method_name)()
        else:
            print(getattr(obj, method_name)())
        sys.stdout = sys.__stdout__
        return output

    def test_str_width_height(self):
        r1 = Rectangle(1, 2)
        prints = TestRectangle_display.printed(r1, "__str__")
        cased = "[Rectangle] ({}) 0/0 - 1/2".format(r1.id)
        self.assertEqual(cased, prints.getvalue().rstrip('\n'))

    def test_display_w_h(self):
        r1 = Rectangle(2, 3)
        prints = TestRectangle_display.printed(r1, "display")
        cased = "##\n##\n##\n"
        self.assertEqual(cased, prints.getvalue())

    def test_display_x(self):
        r1 = Rectangle(2, 3, 1)
        prints = TestRectangle_display.printed(r1, "display")
        cased = " ##\n ##\n ##\n"
        self.assertEqual(cased, prints.getvalue())

    def test_all_display(self):
        r1 = Rectangle(2, 3, 1, 1)
        prints = TestRectangle_display.printed(r1, "display")
        cased = "\n ##\n ##\n ##\n"
        self.assertEqual(cased, prints.getvalue())

if __name__ == "__main__":
    unittest.main()
