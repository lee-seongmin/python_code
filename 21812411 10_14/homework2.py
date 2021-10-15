from tkinter import *
from math import *
#레이블 1개에 버튼이 4개 버튼 구조는 label row=0, button row=1에 column2개 row2에 column2개

def click(key):
    if key =='=':
        result = eval(e.get())
        e.delete(0, END)
        e.insert(END, str(result))
    else:
        e.insert(END,key)
window = Tk()

e = Entry(window)
e.grid(row=0, columnspan=2, sticky='ew',ipadx=100,ipady=25)

button = ["10", "+", "100", "="]
b1 = Button(window,text = "10", command = lambda : click('10')).grid(row=1,column=0, sticky='ew',ipady=25)
b2 = Button(window,text = "+", command = lambda : click('+')).grid(row=1,column=1, sticky='ew',ipady=25)
b3 = Button(window, text = "100", command = lambda : click('100')).grid(row=2,column=0, sticky='ew',ipady=25)
b4 = Button(window,text = "=", command = lambda : click('=')).grid(row=2,column=1, sticky='ew',ipady=25)

e.bind("=",click)
window.mainloop() 