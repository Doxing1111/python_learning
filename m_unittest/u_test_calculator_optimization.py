'''
date: 2021/07/12
author: Joe
'''


import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    # 測試使用案例前置動作
    def setUp(self):
        print('Start Test')

    # 測試使用案例後置動作
    def tearDown(self):
        print('Test End')

    # 測試案例
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

    # 建立測試套件
    suit = unittest.TestSuite()
    suit.addTest(TestCalculator('test_add'))
    suit.addTest(TestCalculator('test_sub'))
    suit.addTest(TestCalculator('test_mul'))
    suit.addTest(TestCalculator('test_div'))

    # 建立測試執行器
    runner = unittest.TextTestRunner()
    runner.run(suit)