from tkinter import *
from math import *
#레이블 1개에 버튼이 4개 버튼 구조는 label row=0, button row=1에 column2개 row2에 column2개

def click(key):
    if key =='10':
        try:
            result = eval(entry.get())
            entry.delete(0, END)
            entry.insert(END, str(result))
        except:
            entry.insert(END, "오류!")
window = Tk()

e = Entry(window)
e.grid(row=0, columnspan=2)

b1 = Button(window,text = "10").grid(row=1,column=0)
b2 = Button(window,text = "+").grid(row=1,column=1)
b3 = Button(window, text = "100").grid(row=2,column=0)
b4 = Button(window,text = "=").grid(row=2,column=1)

e.bind("=",click)
window.mainloop()