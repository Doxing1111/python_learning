'''
date: 2021/07/02
author: Joe
'''

import tkinter as tk

# Tkinter pack 佈局
# 建立視窗
win = tk.Tk()

# 視窗名稱
win.title('Python Learning')

# 視窗大小
win.geometry('600x200')

lbl01 = tk.Label(win, text='Tkinter', bg='pink', font=('標楷體', 36))
lbl02 = tk.Label(win, text='Author', bg='yellow', font=('標楷體', 24))
lbl03 = tk.Label(win, text='Joe', bg='red', fg='white', font=('標楷體', 16))
lbl01.pack()
lbl02.pack()
lbl03.pack()
win.mainloop()

# ============================================================================
# Tkinter grid 佈局方法
win = tk.Tk()
win.title('Python Learning')
win.geometry('600x200')
lbl01 = tk.Label(win, text='Tkinter', bg='pink', font=('標楷體', 36))
lbl02 = tk.Label(win, text='Author', bg='yellow', font=('標楷體', 24))
lbl03 = tk.Label(win, text='Joe', bg='red', fg='white', font=('標楷體', 16))
lbl01.grid(row=0, column=0)
lbl02.grid(row=1, column=1)
lbl03.grid(row=2, column=2)
win.mainloop()

# ============================================================================
def fnHello():
    lblShow['text'] = 'Hello World!'


def fnClear():
    lblShow['text'] = ''


win = tk.Tk()
win.title('按鈕範例')
win.geometry('250x100')
lblShow = tk.Label(win, text='', font=('細明體', 18))
btnHello = tk.Button(win, text='Hello', command=fnHello)
btnClear = tk.Button(win, text='Clear', command=fnClear)
lblShow.pack()
btnHello.pack()
btnClear.pack()
win.mainloop()

# ========================================================================
'''
Entry 範例
定義fnOk函式, 當按下確定鈕會執行此函式
'''

def fnOk():
    vName = name.get()
    vScore = score.get()
    if vScore >= 90 :
        level = 'A'
    elif vScore >= 80:
        level = 'B'
    elif vScore >= 70:
        level = 'C'
    elif vScore >= 65:
        level = 'D'
    else:
        level = 'F'
    lblResult['text'] = '{0}成績是{1},等級是{2}'.format(vName, vScore, level)

win = tk.Tk()
win.title('按鈕範例')

win.geometry('300x150')

# 指定tkinter模組的字串物件name，是txtName文字欄的變數
name=tk.StringVar()

# 指定tkinter模組的整數物件score，是txtScore文字欄的變數
score = tk.IntVar()

# 建立lblName標籤
lblName = tk.Label(win, text='姓名', padx=10, pady=8)
lblName.grid(row=0, column=0)

# 建立txtName文字欄，此文字欄代表變數為name
txtName = tk.Entry(win, width=15, textvariable=name)
txtName.grid(row=0, column=1)

# 建立lblScore標籤
lblScore = tk.Label(win, text='分數', padx=10, pady=8)
lblScore.grid(row=1, column=0)

# 建立txtScore文字欄，此文字欄代表變數為score
txtScore = tk.Entry(win, width=15, textvariable=score)
txtScore.grid(row=1, column=1)

# 建立btnOk按鈕，按下此鈕會執行fnOk函式
btnOk = tk.Button(win, text='確定', command=fnOk)
btnOk.grid(row=2, column=0)

# 建立lblResult標籤
lblResult = tk.Label(win, text='', padx=10, pady=8)
lblResult.grid(row=2, column=1)
win.mainloop()
