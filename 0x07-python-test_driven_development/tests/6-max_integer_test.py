#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""
    def test_noargs(self):
        """no arguments"""
        self.assertEqual(max_integer(), None)

    def test_empty(self):
        """empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """one element only"""
        self.assertEqual(max_integer([10]), 10)

    def test_identicalelements(self):
        """test againt identical items"""
        self.assertEqual(max_integer([12, 12, 12, 12]), 12)

    def test_startmax(self):
        """max element in the start of the list"""
        self.assertEqual(max_integer([10, 3, 2, 1]), 10)

    def test_elments(self):
        """test unordered elments in a list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_large(self):
        """many elements"""
        self.assertEqual(max_integer([100, 333, 1000, 221, 1024, 353, 500,
                                     108, 256, 512]), 1024)

    def test_both(self):
        """positive and negative elements"""
        self.assertEqual(
            max_integer([-23, 58, 91, 24, -1000, -89, 98, 108, -53534562354, -312]),
            108)

    def test_allneg(self):
        """test all negative elements"""
        self.assertEqual(
            max_integer(
                [-6105, -54849, -5553, -3088955, -6711290, -4817844,
                    -1907189, -8110534, -6601769, -5837524, -4726702,
                    -8433749, -7251403, -5117635, -2979207, -1335257,
                    -6266, -9073637, -6224732, -1080801, -1080228,
                    -6801278, -8351954, -1736432, -7131, -4376995,
                    -967891, -4663691, -71562, -7153670, -8038202,
                    -7893047, -9350883, -1132134, -3675971, -8495354,
                    -9158229, -9310087, -6319598, -8961209, -4906000,
                    -386471, -639929, -2676965, -6881679, -6258057,
                    -5477, -1107298, -4199148, -5933601, -9917695,
                    -7759849, -7045734, -4885806, -9485075, -5119579,
                    -4147063, -7622811, -4671971, -59539, -840414,
                    -3671742, -4400074, -3549343, -9146070, -6071672,
                    -7213213, -1307446, -3936098, -2415520, -9162654,
                    -6129976, -5791439, -81890, -7828832, -6954726,
                    -52933, -4952516, -6115545, -8333464, -7271456,
                    -4097027, -4342575, -8400559, -8235052, -4373818,
                    -8054214, -8565596, -639225, -2292452, -4269529,
                    -7202853, -6891036, -4379807, -75196, -1536591,
                    -2833, -25661, -9997, -3620]), -71562)

    def test_ints_and_floats(self):
        """test int all types and floats"""
        self.assertEqual(
            max_integer(
                [10, 99.8, -100, -0.1, 1000, 9999, -100, 998.9]), 9999)

    def test_floats(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [.00123, .457568, .02345, .23423434, .45675674, .678678,
                    .867090, .74653, .5745375]), 0.86709)

    def test_numeric_string(self):
        """test numerical strings"""
        self.assertEqual(max_integer("123456789"), "9")

    def test_string(self):
        """test for strings"""
        self.assertEqual(max_integer("ayman"), "y")

    def test_lists(self):
        """test for lists of lists"""
        self.assertEqual(max_integer([[], [2], [6], [2, 9]]), [6])

    def test_str_list(self):
        """test string lists"""
        self.assertEqual(
            max_integer([["foo"], ["boo"], ["abc"], ["sic"], ["ric"]]),
            ["sic"])

    def test_inf(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([99, float('inf'), float('-inf')]),
                         float('inf'))

    def test_nan(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([99, float('nan'), 100]), 100)

    def test_mixed_list(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([[], [2], [4], [2, 9], 99, "foo"])

    def test_mixed_list_int_str(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([99, "foo"])

    def test_none(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_dict(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([{20: 23, 14: 45}, {"a": "b"}])

    def test_int(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(98)

    def test_float(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(9.8)

if __name__ == '__main__':
    unittest.main()
