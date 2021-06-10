'''
date: 2021/06/03
author: Joe
'''


# 函式
'''
def 函式名稱 ([參數1, 參數2, ......])
    程式區塊
    return  (回傳值1, 回傳值2, ....)
'''

# 範例一
def sayHello():
    print('Hello World')

sayHello() # Hello World


# 範例二
def GetArea(length, width, height):
    area = length * width * height
    print('area =', area) # area = 400
    return area

GetArea(10, 20, 2) # area = 400
x = GetArea(2, 2, 2) # area = 8
print('x =', x) # x = 8


# 範例三 (攝氏[Celsius]溫度轉華氏[Fahrenheit]溫度)
def ctof(c):
    f = c * 1.8 + 32
    return f

inputc = float(input('請輸入攝氏溫度: '))
print('華氏溫度為: %4.1f 度' % ctof(inputc))


# 不訂數目參數函式
def calsum(*params):
    total = 0
    for param in params:
        total += param
    return total

print('1 個參數: calsum(2) = %d' % calsum(2)) # 1 個參數: calsum(2) = 2
print('2 個參數: calsum(2,5) = %d' % calsum(2,5)) # 2 個參數: calsum(2,5) = 7
print('3 個參數: calsum(2,5,7) = %d' % calsum(2,5,7)) # 3 個參數: calsum(2,5,7) = 14


# 全域變數、區域變數
# 有相同名稱的全域變數與區域變數, 以區域變數為先
# 在函式內, 會使用區域變數; 函式外, 因區域變數不存在, 故使用全域變數
def scope():
    var1 = 1
    print(var1, var2) # 1, 20 (函式中沒有 var2 變數, 故使用全域變數 var = 20

var1 = 10
var2 = 20

scope()
print(var1, var2) # 10, 20

# 在函式內使用全域變數, 需在函式中以 global 宣告
def scope():
    global var1
    var1 = 1
    var2 = 2
    print(var1, var2) # 1, 2

var1 = 10
var2 = 20

scope()
print(var1, var2) # 1, 20