'''
date: 2021/05/25
author: Joe
'''

# 函式 Function
sum = 0

def display(n):
    print('第 ' + str(n) + ' 次執行迴圈')

for i in range(1,11):
    display(i)
    sum += i
    print(sum) # 查看每次加總的值

print('1+2+3+....+10 = ' + str(sum))

# ===============================================
# format 格式化 =  %s(字串)、 %d(整數)、 %f(浮點數)
print("姓名    座號    國文    數學    英文")
print("%3s  %2d     %3d     %3d     %3d" % ("周星祖", 11, 95, 100, 80))

# ===============================================
# if 多向判斷式
score = int(input('請輸入成績: '))
if score >= 90:
    print('優等')
elif score >= 80:
    print('甲等')
elif score >= 70:
    print('乙等')
elif score >= 60:
    print('丙等')
else:
    print('丁等')

# ===============================================
money = int(input('請輸入購物總金額: '))
if money >= 10000:
    if money >= 100000:
        print(money * 0.8, end=' 元')
    elif money >= 50000:
        print(money * 0.85, end=' 元')
    elif money >= 30000:
        print(money * 0.9, end=' 元')
    else:
        print(money * 0.95, end=' 元')
else:
    print('您的購物總金額未達打折條件')

# ===============================================
country = input('請問您來至美國或台灣: ')
age = input('請輸入年齡: ')
age = int(age)
if country == '台灣':
    if age >= 18:
        print('你可以考取駕照')
    else:
        print('你還不能考取駕照')
elif country == '美國':
    if age >= 16:
        print('你可以考取駕照')
    else:
        print('你還不能考取駕照')
else:
    print('請輸入美國或台灣')

# ================================================
# BMI計算的程式
height = input('請輸入身高(cm)： ')
weight = input('請輸入體重(kg)： ')
height = int(height)
weight = int(weight)
height = height / 100 # 換成公尺
bmi = weight / height / height
if bmi < 18.5:
    print('你的bmi值為', bmi, '屬體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print('你的bmi值為', bmi, '屬正常範圍')
elif bmi >= 24 and bmi < 27:
    print('你的bmi值為', bmi, '稍重')
elif bmi >= 27 and bmi < 30:
    print('你的bmi值為', bmi, '輕度肥胖')
elif bmi >= 30 and bmi < 35:
    print('你的bmi值為', bmi, '中度肥胖')
elif bmi >= 35: # 寫else: 也可以
    print('你的bmi值為', bmi, '重度肥胖')
