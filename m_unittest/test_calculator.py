'''
date: 2021/07/10
author: Joe
'''


'''
此測試案例無導入 unittest 單元測試架構來執行, 有幾個缺點:
1.需自行定義斷言失敗後的提示
2.當一個測試函數執行失敗後, 後面的測試函數將不在執行
3.執行結果無法統計   
'''

from calculator import Calculator

def test_add():
    c = Calculator(2, 5)
    result = c.add()
    assert result == 7, '加法運算失敗' # 如結果非8, 會顯示 AssertionError: 加法運算失敗

def test_sub():
    c = Calculator(2, 2)
    result = c.sub()
    assert result == 0, '減法運算失敗'

def test_mul():
    c = Calculator(6, 7)
    result = c.mul()
    assert result == 42, '乘法運算失敗'

def test_div():
    c = Calculator(5, 5)
    result = c.div()
    assert result == 1, '除法運算失敗' # 這邊


if __name__ == '__main__':
    test_add()
    test_sub()
    test_mul()
    test_div()
