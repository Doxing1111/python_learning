# 函式 Function

sum = 0

def display(n):
    print('第 ' + str(n) + ' 次執行迴圈')

for i in range(1,11):
    display(i)
    sum += i
    print(sum) # 查看每次加總的值

print('1+2+3+....+10 = ' + str(sum))

#===============================================

# format 格式化 =  %s(字串)、 %d(整數)、 %f(浮點數)
print("姓名    座號    國文    數學    英文")
print("%3s  %2d     %3d     %3d     %3d" % ("周星祖", 11, 95, 100, 80))
