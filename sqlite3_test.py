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

# 再新增一筆
num = 2
tel = '02-22226666'
sqlstr = 'insert into table01 values ({}, "{}")'.format(num, tel)
cursor.execute(sqlstr)

# 修改資料
sqlstr = 'update table01 set tel = "05-555666" where num=2'
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


