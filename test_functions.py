import unittest
import math  #для работы с математическими константами
from taylor_functions import TaylorFunctions
from main_function import MainFunction

class TestTaylorFunctions(unittest.TestCase):
    def test_sin(self):
        self.assertAlmostEqual(TaylorFunctions.sin(0), 0, places=5)
        self.assertAlmostEqual(TaylorFunctions.sin(math.pi / 2), 1, places=5)
        self.assertAlmostEqual(TaylorFunctions.sin(-math.pi / 2), -1, places=5)
        self.assertAlmostEqual(TaylorFunctions.sin(math.pi), 0, places=5)

    def test_cos(self):
        self.assertAlmostEqual(TaylorFunctions.cos(0), 1, places=5)
        self.assertAlmostEqual(TaylorFunctions.cos(math.pi), -1, places=5)
        self.assertAlmostEqual(TaylorFunctions.cos(math.pi / 2), 0, places=5)

    def test_ln(self):
        self.assertAlmostEqual(TaylorFunctions.ln(1), 0, places=5)
        self.assertAlmostEqual(TaylorFunctions.ln(math.e), 1, places=5)
        self.assertAlmostEqual(TaylorFunctions.ln(0.5), math.log(0.5), places=5)
        with self.assertRaises(ValueError):
            TaylorFunctions.ln(-1)

class TestMainFunction(unittest.TestCase):
    def test_f_positive_x(self):
        self.assertAlmostEqual(MainFunction.f(1), TaylorFunctions.ln(1 + 1e-10) * TaylorFunctions.cos(1), places=5)
        self.assertAlmostEqual(MainFunction.f(2), TaylorFunctions.ln(2) * TaylorFunctions.cos(2), places=5)

    def test_f_negative_x(self):
        self.assertAlmostEqual(MainFunction.f(-1), (abs(TaylorFunctions.sin(-1)) - TaylorFunctions.cos(-1)) / (TaylorFunctions.ln(1 + 1e-10) + 1), places=5)
        self.assertAlmostEqual(MainFunction.f(-2), (abs(TaylorFunctions.sin(-2)) - TaylorFunctions.cos(-2)) / (TaylorFunctions.ln(2) + 1), places=5)

    def test_f_zero(self):
        self.assertAlmostEqual(MainFunction.f(0), TaylorFunctions.ln(1e-10) * TaylorFunctions.cos(0), places=5)
