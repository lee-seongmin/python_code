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