'''
date: 2021/06/15
author: Joe
'''

import manage as m

m.data = dict() # 建立 data 為字典型別的全域變數
m.data = m.ReadData()  # 讀取文字檔後轉換為 dict



while True:
    m.menu()
    choice = int(input("請選擇所需的服務： "))
    print()
    if choice == 1:
        m.input_data()
    elif choice == 2:
        m.disp_data()
    elif choice == 3:
        m.edit_data()
    elif choice == 4:
        m.delete_data()
    else:
        break

print("程式已關閉！")