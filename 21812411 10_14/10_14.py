from tkinter import*

window = Tk() # root window생성

label = Label(window, text="Hello World! ") # Label(텍스트, 이미지용) 위젯 생성
label.pack() # 텍스트를 표기할정도로만 크기를 축소 후 출력
window.mainloop() #윈도우 이벤트를 처리 시작
#%%
b1 = Button(window, text="이것이 파이썬 버튼입니다.")
b1.pack()
window.mainloop()
#%%
from tkinter import *

window = Tk()
b1 = Button(window, text = "첫번째 버튼") # b1.pack(side=LEFT, padx=10) :x축방향 픽셀추가
b2 = Button(window, text = "두번째 버튼") # b2.pack(side=LEFT, padt=10) :y축방향 픽셀추
b1.pack(side=LEFT,padx=10)
b2.pack(side=LEFT,padx=10)
b1["text"]="One" # dictionary의 키와 비슷하다.
b2["text"]="Two"
window.mainloop()
#%%
from tkinter import *

def callback():
    button["text"] = "버튼이 클릭되었음"
    
window = Tk()
button = Button(window,text= "클릭", command = callback) # 명령을 줄 때 command=함수이름
button.pack(side=LEFT)

window.mainloop()
#%%
from tkinter import *

class App:
    def __init__(self):
        window = Tk()
        helloB = Button(window, text="Hello", command = self.hello, fg="red") # 얘는 윈도우에 작동하는게 아니라 콘솔에 작동 bg=배경, fg=전경
        helloB.pack(side=LEFT)
        quitB = Button(window,text="Quit", command = self.quit())
        quitB.pack(side=LEFT)
        window.mainloop()
    def hello(self):
        print("Hello 버튼이 클릭되었음!")
    def quit(self):
        print("Quit 버튼이 클릭되었음!") #내장함수와 자신이 만든 함수가 중복될 경우 자신이 만든 함수를 먼저 사용한다.

app=App()
#%%
import tkinter as tk
import tkinter.font as font

class App:
    def __init__(self):
        root = tk.Tk() #root window
        self.customFont = font.Font(family="Helvetica", size=12)
    
        #buttonframe = tk.Frame() #
        label = tk.Label(root,text = "Hello", font = self.customFont)
        label.pack()
        
        bigger = tk.Button(root, text ="폰트를 크게", command = self.BigFont)
        smaller = tk.Button(root, text = '폰트를 작게', command= self.smallFont)
        bigger.pack()
        smaller.pack()
        window.mainloop()
    def BigFont(self):
        size = self.customFont["size"]
        self.customFont.config(size = size + 2)
    def SmallFont(self):
        size = self.customFont["size"]
        self.customFont.config(size = size-2)
#%%
from tkinter import *

window = Tk()
Label(window, text = "이름").grid(row=0)
Label(window, text = "나이").grid(row=1)

e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

#%%
from tkinter import *

def show():
    print("이름 : %s\n 나이 : %s " % (e1.get(),e2.get()))

parent = Tk()
Label(parent, text = "이름").grid(row=0)
Label(parent, text = "나이").grid(row=1)

e1 = Entry(parent)
e2 = Entry(parent)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(parent, text = "보이기", command =show).grid(row=3, column=1, sticky = W, pady = 4)
Button(parent, text = "종료", command =parent.quit).grid(row=3, column=0, sticky = W, pady = 4)

mainloop()
# %%
from tkinter import *
from math import *

def calculate(event):
    label.configure(text = "결과: " +str(entry.get()))
window = Tk()
Label(window, text = "파이썬 수식 입력: ").pack()

e = Entry(window)
e.bind("<Return>",calculate)
e.pack()

label = Label(window,text = "결과: ")
label.pack()

window.mainloop()
#%%