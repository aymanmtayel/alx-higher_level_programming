#!/usr/bin/python3
"""Unittest for rectangle module"""


import unittest
import io
import sys
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class TestSquare(unittest.TestCase):
    """unittest for rectangle class"""

    def test_rectangle_exist(self):
        r1 = Square(2)
        self.assertEqual(r1.size, 2)

    def test_r_x_only(self):
        r1 = Square(1, 2)
        self.assertEqual(r1.size, 1)
        self.assertEqual(r1.x, 2)

    def test_r_x_y(self):
        r1 = Square(1, 2, 3)
        self.assertEqual(r1.size, 1)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)

    def test_r_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1", 2)

    def test_r_height_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_r_x_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_r_all_args(self):
        r1 = Square(1, 2, 3, 4)
        self.assertEqual(r1.size, 1)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 4)

    def test_r_neg_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_r_neg_height(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_r_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)

    def test_r_neg_x(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_r_area_with_all_args(self):
        r1 = Square(3, 2, 3, 4)
        self.assertEqual(r1.area(), 9)

class TestSquare_display(unittest.TestCase):
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

    def test_str_size(self):
        r1 = Square(1)
        prints = TestSquare_display.printed(r1, "__str__")
        cased = "[Square] ({}) 0/0 - 1".format(r1.id)
        self.assertEqual(cased, prints.getvalue().rstrip('\n'))

    def test_display_w_h(self):
        r1 = Square(2)
        prints = TestSquare_display.printed(r1, "display")
        cased = "##\n##\n"
        self.assertEqual(cased, prints.getvalue())

    def test_display_x(self):
        r1 = Square(2, 3)
        prints = TestSquare_display.printed(r1, "display")
        cased = "   ##\n   ##\n"
        self.assertEqual(cased, prints.getvalue())

    def test_all_display(self):
        r1 = Square(2, 3, 1)
        prints = TestSquare_display.printed(r1, "display")
        cased = "\n   ##\n   ##\n"
        self.assertEqual(cased, prints.getvalue())

class TestSquare_dictionary(unittest.TestCase):
    """class for testing dictionaries in Square"""

    def test_to_dictionary_all_n(self):
        r1 = Square(1, 2, 3 ,4)
        printed = {'size': 1, 'x': 2, 'y': 3, 'id': 4}
        self.assertEqual(printed, r1.to_dictionary())

class TestSquare_update(unittest.TestCase):
    """class for testing update values in rectangle class"""

    def test_update_id(self):
        r1 = Square(1, 2, 3, 4)
        r1.update(89)
        self.assertEqual("[Square] (89) 2/3 - 1", str(r1))

    def test_update_id_s(self):
        r1 = Square(2, 2, 3, 4)
        r1.update(89, 1)
        self.assertEqual("[Square] (89) 2/3 - 1", str(r1))

    def test_update_id_s_x(self):
        r1 = Square(3, 4, 3, 4)
        r1.update(89, 1, 2)
        self.assertEqual("[Square] (89) 2/3 - 1", str(r1))

    def test_update_id_s_x_y(self):
        r1 = Square(5, 5, 5, 5)
        r1.update(89, 1, 2, 3)
        self.assertEqual("[Square] (89) 2/3 - 1", str(r1))

    def test_update_kwarg_id(self):
        r1 = Square(1, 2, 3, 4)
        r1.update(**{'id': 89})
        self.assertEqual("[Square] (89) 2/3 - 1", str(r1))

    def test_update_kwarg_id_size(self):
        r1 = Square(2, 2, 3, 4)
        r1.update(**{'id':89, 'size': 1})
        self.assertEqual("[Square] (89) 2/3 - 1", str(r1))

    def test_update_kwarg_id_size_x(self):
        r1 = Square(2, 3, 3, 4)
        r1.update(**{'id':89, 'size': 1, 'x': 2})
        self.assertEqual("[Square] (89) 2/3 - 1", str(r1))

    def test_update_kwarg_id_width_height(self):
        r1 = Square(2, 3, 50, 60)
        r1.update(**{'id':89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual("[Square] (89) 2/3 - 1", str(r1))

class TestSquare_create(unittest.TestCase):
    """class for testing create values in Square class"""
    def test_create_id(self):
        r1 = Square.create(**{"id": 89})
        self.assertEqual("[Square] (89) 1/0 - 1", str(r1))

    def test_create_id_width(self):
        r1= Square.create(**{"id": 89, "size": 2})
        self.assertEqual("[Square] (89) 1/0 - 2", str(r1))
    
    def test_create_id_width_height(self):
        r1= Square.create(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual("[Square] (89) 2/0 - 1", str(r1))

    def test_create_id_width_height_x_y(self):
        r1= Square.create(**{"id": 89, "size": 1, "x": 10, "y":20})
        self.assertEqual("[Square] (89) 10/20 - 1", str(r1))

import unittest
import os
import json
from models.base import Base
class TestSquare_save(unittest.TestCase):
    """class for testing saving to file for Square Module"""

    def cleaner(self):
        # Clean up any existing file before each test
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_save_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            data = json.load(file)
            loaded = Square.load_from_file()
            self.assertEqual(data, [])
            self.assertEqual(type(loaded), list)
            self.assertEqual(len(loaded), len(data))

    def test_save_normal(self):
        r1 = Square(1, 2)
        Square.save_to_file([r1])
        with open("Square.json", "r") as file:
            data = json.load(file)
        self.assertEqual(data, [{"id": r1.id, "size": r1.size, "x": r1.x, "y": r1.y}])



if __name__ == "__main__":
    unittest.main()
