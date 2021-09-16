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
