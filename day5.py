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
list2 = ['Apple', 'Banana', 'Orange']
tuple4 = tuple(list2)
tuple4.append(8) # AttributeError: 'tuple' object has no attribute 'append'
print(tuple4)

# ==========================================================================
# dict (字典) 取得元素值以鍵作為索引來取得值
# dict = {鍵1:值1, 鍵2:值2}
dict1 = {'Apple':15, 'Banana':25, 'Orange':35}
print(dict1['Apple']) # 15
print(dict1['Orange']) # 35
dict1['Banana'] = 40
print(dict1['Banana']) # 40

# del 刪除字典特定元素
del dict1['Orange']
print(dict1) # {'Apple':15, 'Banana':40}

# 字典名稱.clear() 刪除字典所有元素
dict1.clear()
print(dict1) # {}

# 以 keys 與 values 方法取得 [鍵] 與 [值] 的組合, 並轉換成串列
dict1 = {'Mark':90, 'Jobs':40, 'Allen':85}
dict1['Joe'] = 100
dict1['Odin'] = 60
listkey = list(dict1.keys()) # 以 [鍵] 為元素的組合
listvalue = list(dict1.values()) # 以 [值] 為元素的組合
for i in range(len(listkey)):
    print('%s 的成績為: %d 分' % (listkey[i], listvalue[i]))


# items() 方法可取得所有 [鍵-值]
dict1 = {'Mark':90, 'Jobs':40, 'Allen':85}
dict1['Joe'] = 100
dict1['Odin'] = 60
listitem = dict1.items()
for name, score in listitem:
    print(('%s 的成績為: %d 分' % (name, score)))

'''
Mark 的成績為: 90 分
Jobs 的成績為: 40 分
Allen 的成績為: 85 分
Joe 的成績為: 100 分
Odin 的成績為: 60 分
'''

# get (鍵如果存在, 不論是否有設定預設值, 接傳回字典中對應的值
dict1 = {'Apple':50, 'Banana':20, 'Orange':35}
dict1.get('Apple') # 50
dict1.get('Apple', 100) # 50
dict1.get('Watermelon') # None
dict1.get('Watermelon', 80) # 80
print(dict1) # {'Apple': 50, 'Banana': 20, 'Orange': 35}

# setdefault (若[鍵]不存在, 則會將[鍵-值]對加入字典作為元素
dict1 = {'Apple':50, 'Banana':20, 'Orange':35}
dict1.setdefault('Apple', 100) # 50
dict1.setdefault('Watermelon') # None
dict1.setdefault('Watermelon', 65)
print(dict1) # {'Apple': 50, 'Banana': 20, 'Orange': 35, 'Watermelon': 65}


# dictget.py
dict1 = {'A':'內向', 'B':'外向', 'O':'堅強', 'AB':'聰明'}
name = str.upper(input("請輸入查詢的血型: "))  # upper 將小寫字母轉換為大寫字母
blood = dict1.get(name)

print(blood)

if blood == None:
    print("沒有「" + name + "」血型！")
else:
    print(name + "血型的個性 " + dict1[name])