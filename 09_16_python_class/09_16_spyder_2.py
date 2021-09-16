# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:08:04 2021

@author: pc03
"""
ans=0
hap=0
for i in range(0,100):
    if(i%3==0):
        ans+=1
        hap+=i

print("1부터 100사이의 모든 값은 {0}".format(hap))
print("1부터 100사이의 3의배수의 개수는 {0}".format(ans))
#%%
import random
com_ans=random.random(1,101)

print("숫자게임에 오신것을 환영합니다.")

cnt=0
btn='Y' or 'y'

while(btn=='y' or 'Y'):
    if(btn=='y' or btn=='Y'):
        ans=int(input("숫자를 맞춰 보세요 : "))
    
        if(ans>com_ans):
            print("너무 큼!")
        elif(ans<com_ans):
            print("작음!")
        else:
            print("!맞췄습니다!")
        cnt+=1
        print("{0}회차 시도".format(cnt))
    else:
        break
    
    btn=(str(input("계속하시겠습니까?")))
    
#%%

import turtle as t
T= t.Turtle()
import math

#x1=math.radians()
t.pendown()
t.shape("turtle")
for x in range(0,361):
    y=math.sin(math.radians(x))
    scaledX=x
    scaledY=y*100
    t.goto(scaledX,scaledY)
t.penup()
t.goto(0,math.cos(math.radians(0)))

t.pendown()
for x in range(0,361):
    y=math.cos(math.radians(x))
    scaledX=x
    scaledY=y*100
    t.goto(scaledX,scaledY)

t.penup()

#%%

import turtle as t
T= t.Turtle()
#import math
import numpy as np

t.shape("turtle")
t.penup()
t.goto(-100, 1 / (1+np.exp(-2*-100)))
t.pendown()
for x in range(-100,101):
    y=1 / (1+np.exp(-2*x))
    scaledX=x
    scaledY=y*100
    t.goto(scaledX,scaledY)
t.penup()
