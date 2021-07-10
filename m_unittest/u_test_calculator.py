'''
date: 2021/07/10
author: Joe
'''

'''透過 unittest 單元測試架構重寫測試案例'''

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        c = Calculator(5, 5)
        result = c.add()
        self.assertEqual(result, 10)

    def test_sub(self):
        c = Calculator(6, 1)
        result = c.sub()
        self.assertEqual(result, 5)

    def test_mul(self):
        c = Calculator(2, 2)
        result = c.mul()
        self.assertEqual(result, 5)

    def test_div(self):
        c = Calculator(6, 3)
        result = c.div()
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()


