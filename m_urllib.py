'''
date: 2021/07/04
author: Joe
'''

# 利用 urllib 模組的 urlparse 函式，解析網址
from urllib.parse import urlparse

url = 'https://tw.news.yahoo.com/topic/2019-nCoV'
o = urlparse(url)
print(o)

print("scheme={}".format(o.scheme)) # 傳回通訊協定 https
print("netloc={}".format(o.netloc)) # 傳回網址名稱 tw.news.yahoo.com
print("path={}".format(o.path)) # 傳回路徑 /topic/2019-nCoV
print("params={}".format(o.params)) # 傳回 url 查詢參數字串，不存在傳回空字串
print("query={}".format(o.query)) # 傳回 query 查詢字串，即 GET 的參數，不存在傳回空字串
print("fragment={}".format(o.fragment)) # 傳回框架名稱，不存在傳回空字串
print("port={}".format(o.port)) # 傳回通訊埠，不存在傳回None


