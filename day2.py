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
# score = int(input('請輸入成績: '))
# if score >= 90:
#     print('優等')
# elif score >= 80:
#     print('甲等')
# elif score >= 70:
#     print('乙等')
# elif score >= 60:
#     print('丙等')
# else:
#     print('丁等')

# ===============================================
money = int(input('請輸入購物總金額: '))
if money >= 10000:
    if money >= 100000:
        print(money * 0.8, end = ' 元')
    elif money >= 50000:
        print(money * 0.85, end = ' 元')
    elif money >= 30000:
        print(money * 0.9, end = ' 元')
    else:
        print(money * 0.95, end = ' 元')
else:
    print('您的購物總金額未達打折條件')
