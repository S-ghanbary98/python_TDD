
import unittest
import pytest

from simple_calc import SimpleCalc



class Cacltest(unittest.TestCase):
    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(3,2), 5)
        #return num1 + num2

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3,2), 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4) # 2 * 2 = 4

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)  # 6 / 3 = 2
