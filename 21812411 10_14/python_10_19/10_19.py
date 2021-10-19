from tkinter import *
window = Tk()
canvas = Canvas(window, width = 400, height = 300)
canvas.pack()
id = canvas.create_oval(10, 100, 50, 150, fill = 'green')

def move_right(event):
    canvas.move(id,5,0)
canvas.bind_all('<KeyPress-Right>', move_right)

def move_left(event):
    canvas.move(id,-5,0)
canvas.bind_all('<KeyPress-Left>', move_left)

def move_upward(event):
    canvas.move(id,0,-5)
canvas.bind_all('<KeyPress-Up>', move_upward)

def move_down(event):
    canvas.move(id,0,5)
canvas.bind_all('<KeyPress-Down>', move_down)

def move_northwestward(event):
    canvas.move(id,5,0)
canvas.bind_all('<KeyPress-Right>', move_right)

window.mainloop()

#%%
from tkinter import *

w = 500
h = 300

def drawDot(event):
    x1, y1 = (event.x-1), (event.y-1)
    x2, y2 = (event.x+1), (event.y+1)
    canvas.create_oval(x1, y1,x2,y2, fill="red")
window = Tk()
canvas = Canvas(window, width = w, height = h)
canvas.pack(expand = YES, fill = BOTH)
canvas.bind("<B1-button>", drawDot)

message = Label(window, text = "마우스를 드래그하면 점들이 그려집니다.")
message.pack(side = BOTTOM)

window.mainloop()
#%%
from tkinter import *
window = Tk()
b1 = Button(window, text = "첫번째버튼")
b1.pack(side = LEFT, padx = 10)
b1["text"] = "one"
window.mainloop()
#%%
from tkinter import *
window = Tk()

button_list=[]

for a in range(9):
    button_list.append(a)

for k in range(9):
     buttonlist[k]= Button(window, text= f"{k}번째 버튼")
    
for i in range(3):
    for j in range(3):
        button_list[(j)*(i+1)].grid(row = i,column = j)
        
        
window.mainloop()
#%%
from tkinter import *

def checked(i):
    global player
    button = button_l[i]
    
    if button["text"] != "     ":
        return
    button["text"] = "  " + player + "  "
    button["bg"] = "yellow"
    if player == 'X':
        player = "O"
        button["bg"] = "yellow"
    else:
        player = "X"
        button["bg"] = "lightgreen"
window = Tk()
player = "X"
button_l = []
player_list = []
for i in range(9):
    b = Button(window, text = "     ", command = lambda k=i:checked(k) , width = 10, height = 10)
    b.grid(row = i // 3, column = i % 3)
    button_l.append(b)
    player_list.append(player)
window.mainloop()


if player_list[len(player_list)]