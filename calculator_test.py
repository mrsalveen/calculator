import unittest
import calculator


class TestStringMethods(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(calculator.addition(''), 0)

    def test_one_number(self):
        self.assertEqual(calculator.addition('14'), 14)

    def test_two_comma(self):
        self.assertEqual(calculator.addition('12,4'), 16)
        
    def test_new_line(self):
        self.assertEqual(calculator.addition('12\n4'), 16)

    def test_three(self):
        self.assertEqual(calculator.addition('12,4\n4'), 20)

