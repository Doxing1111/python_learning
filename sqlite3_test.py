'''
date: 2021/06/25
author: Joe
'''

import sqlite3

# 建立資料庫連線
conn = sqlite3.connect('test1.sqlite')

# 建立 cursor 物件
cursor = conn.cursor()

# 建立資料表
sqlstr = 'CREATE TABLE IF NOT EXISTS table01 \
         ("num" INTEGER PRIMARY KEY NOT NULL, "tel" TEXT)'
cursor.execute(sqlstr)

# 新增資料
sqlstr= 'insert into table01 values (1, "04-22223310")'
cursor.execute(sqlstr)

# 再新增一筆
num = 2
tel = '02-22226666'
sqlstr = 'insert into table01 values ({}, "{}")'.format(num, tel)
cursor.execute(sqlstr)

# 修改資料
sqlstr = 'update table01 set tel = "05-55556666" where num=2'
cursor.execute(sqlstr)

# 刪除資料
sqlstr = "delete from table01 where num=1"
conn.execute(sqlstr)

# 刪除資料表
sqlstr = "DROP TABLE table01"
conn.execute(sqlstr)

# 主動更新
conn.commit()

# 關閉資料庫連線
conn.close()

# =====================================================================
cursor = conn.execute('select * from table01')
rows = cursor.fetchall() # 以二維串列方式取得資料表資料
print(rows) # fetchall() 顯示資料表所有的資料, 每一列資料都是一筆元組資料 [(1, '04-22223310'), (2, '02-22226666')]
for row in rows:
    print("{}\t{}".format(row[0], row[1])) # 用 row[0]、row[1] 取得資料表前面兩個欄位

# =====================================================================
cursor = conn.execute('select * from table01 where num=1')
row = cursor.fetchone() # 以串列方式取得資料表資料
if not row == None:
    print("{}\t{}".format(row[0], row[1]))  # 1	04-22223310

