import ast


def menu():
    print("帳號、密碼管理系統")
    print("-------------------------")
    print("1. 新增帳號、密碼")
    print("2. 顯示帳號、密碼")
    print("3. 修  改  密  碼")
    print("4. 刪除帳號")
    print("0. 結  束  程  式")
    print("-------------------------")


def ReadData():
    with open('password.txt', 'r', encoding='UTF-8-sig') as f:  # windows對於utf-8格式的檔案儲存預設是帶有BOM的格式
        filedata = f.read()
        if filedata != "":
            data = ast.literal_eval(filedata)
            return data
        else:
            return dict()


def disp_data():
    print("帳號\t密碼")
    print("================")
    for key in data:
        print("{}\t{}".format(key, data[key]))
    input("請按<Enter>鍵返回主選單")


def input_data():
    while True:
        name = input("請輸入欲新增的帳號 (輸入完成請按<Enter>鍵): ")
        if name == "":
            break
        if name in data:
            print("{} 帳號已存在！".format(name))
            continue
        password = input("請輸入密碼 (輸入完成請按<Enter>鍵): ")
        data[name] = password
        with open('password.txt', 'w', encoding='UTF-8-sig') as f:
            f.write(str(data))
        input("帳號已新增完成！請按<Enter>鍵返回主選單")
        break


def edit_data():
    while True:
        name = input("請輸入要修改的帳號 (輸入完成請按<Enter>鍵): ")
        if name == "":
            break
        if not name in data:
            print("{} 帳號不存在！".format(name))
            continue
        print("原來密碼為：{}".format(data[name]))
        password = input("請輸入新密碼：")
        data[name] = password
        with open('password.txt', 'w', encoding='UTF-8-sig') as f:
            f.write(str(data))
            input("密碼更改完畢！請按<Enter>鍵返回主選單")
            break


def delete_data():
    while True:
        name = input("請輸入要刪除的帳號 (輸入完成請按<Enter>鍵): ")
        if name == "":
            break
        if not name in data:
            print("{} 帳號不存在！".format(name))
            continue
        print("確定刪除 {} 的資料！：".format(name))
        yn = input("(Y/N)? ")
        if yn == "Y" or yn == "y":
            del data[name]
            with open('password.txt', 'w', encoding='UTF-8-sig') as f:
                f.write(str(data))
                input("已刪除完畢！請按<Enter>鍵返回主選單")
                break
