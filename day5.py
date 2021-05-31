'''
date: 2021/05/31
author: Joe
'''

# 一維串列
list1 = [1, 2, 3, 4, 5]
list2 = ['Banana', 'Apple', 'Orange']
print('list1={1}, list2{0}'.format(list1, list2)) # list1 = ['Banana', 'Apple', 'Orange'], list2 = [1, 2, 3, 4, 5]

# 二維串列
list3 = [['Mark', 23], ['John', 32], ['Alex', 41]]
print(list3[1][0])  # John

# append 增加元素 (加在串列最後面)
list4 = [1,2,3,4,5,6]
list4.append(7)
print(list4) # [1, 2, 3, 4, 5, 6, 7]

# extend 增加元素 (加在串列最後面) 只能加串列
list4.extend([8, 9])
print(list4) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# insert 增加元素 (將元素加在串列指定位置)
list4.insert(4, 10)
print(list4) # [1, 2, 3, 4, 10, 5, 6, 7, 8, 9]

# pop 由串列中取出元素, 同時串列會將該元素移除
list5 = [1, 2, 3, 4, 5]
n = list5.pop(2)
print(n) # 3

x = list5.pop() # 沒參數則取出最後一個元素
print(x) # 5

# ======================================================================
# tuple (元組)
tuple1 = (1, 2, 3, 4, 5)
print(len(tuple1)) # 顯示列表元素個數 5

tuple2 = (1, 'Joe', True)
print(tuple2[1]) # Joe

# 元祖轉換串列, 可新增元素
tuple3 = (2, False, 'Allen')
list1 = list(tuple3)
list1.append('Mark')
print(list1) # [2, False, 'Allen', 'Mark']

# 串列轉換元祖, 元祖不能增加元素
# list2 = ['Apple', 'Banana', 'Orange']
# tuple4 = tuple(list2)
# tuple4.append(8) # AttributeError: 'tuple' object has no attribute 'append'
# print(tuple4)

# ==========================================================================
# dict (字典) 取得元素值以鍵作為索引來取得值
# dict = {鍵1:值1, 鍵2:值2}
dict1 = {'Apple':15, 'Banana':25, 'Orange':35}
print(dict1['Apple']) # 15
print(dict1['Orange']) # 35
print(dict1)





