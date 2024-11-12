import convert
import unittest

class Lab7unittests(unittest.TestCase):

    def test_1(self):
        result = convert.str_to_float("201234124")
        check = 201234124
        self.assertEqual(check, result)

    def test_2(self):
        result = convert.str_to_float("Hello")
        check = None
        self.assertEqual(check, result)

