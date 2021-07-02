'''
date: 2021/07/02
author: Joe
'''

# 例外處理
try:
    # n = 5
    print(n)
except:
    print('變數 n 不存在') # 當程式出現異常時, 執行這段程式碼

# =============================
# 範例二
try:
    a = int(input("請輸入第一個整數："))
    b = int(input("請輸入第二個整數：")) # 輸入 ...
    r = a * b
    print("r =", r)

# 方法1 顯示自訂之錯誤訊息
except ValueError:
    print("發生輸入非數值的錯誤!")

# 方法2 顯示系統之錯誤訊息
except Exception as e:
    print("發生", e, "的錯誤!") # 發生 invalid literal for int() with base 10: '...' 的錯誤!

finally:
    print("一定會執行的程式區塊")