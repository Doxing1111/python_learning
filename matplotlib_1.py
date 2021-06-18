'''
date: 2021/06/18
author: Joe
'''

# 範例一
import matplotlib.pyplot as plt

listx1 = [1, 5, 7, 9, 13, 16]
listy1 = [15, 50, 80, 40, 70, 50]
plt.plot(listx1, listy1, label="Male")

listx2 = [2, 6, 8, 11, 14, 16]
listy2 = [10, 40, 30, 50, 80, 60]
plt.plot(listx2, listy2, color='red', linewidth=5, linestyle="--", label="Female")

plt.legend()
plt.xlim(0, 20)
plt.ylim(0, 100)
plt.title('Pocket Money') # 團表標題
plt.xlabel('Age') # x座標標題
plt.ylabel('Money') # y座標標題
plt.show()

# 文件命名不要是 matplotlib.py, 會導致無法導入 matplotlib 庫

# ===================================================================================

# 範例二
import matplotlib.pyplot as plt

year = [2016, 2017, 2018, 2019, 2020] # X軸
city1 = [100, 180, 90, 220, 150] # Y軸
plt.plot(year, city1, 'r-.s', lw=2, ms=10, label="台北") # 第一條線

city2 = [160,50,120,140,110]
plt.plot(year, city2, 'g--*', lw=2, ms=10, label="高雄") # 第二條線

plt.legend() # 顯示數據的名稱
plt.ylim(0, 250) # 範圍
plt.xticks(year) # 標度
plt.title("銷售報表", fontsize=18)
plt.xlabel("年度", fontsize=12)
plt.ylabel("百萬", fontsize=12)
plt.grid(color='k', ls='--', lw=1, alpha=0.5) # 格線

# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 也可設mingliu或DFKai-SB
plt.rcParams["axes.unicode_minus"] = False
plt.show()

# ==================================================================================

範例三
import matplotlib.pyplot as plt

listx = ['c', 'c++', 'c#', 'java', 'python']
listy = [45, 28, 38, 32, 50]
plt.bar(listx, listy, width=0.5, color='rgb')
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")

# 設定中文字型
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"
plt.show()
# ================================================================================

# 範例四
price = [30, 40, 50, 80, 100]
tprice = []
for item in price:
    tprice.append(item * 1.05)
print(tprice)


# 範例四 (串列生成式)
price = [30, 40, 50, 80, 100]
price_list = [item * 1.05 for item in price]
print(price_list)


