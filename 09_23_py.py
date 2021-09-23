# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:59:32 2021

@author: pc03
"""
import time

cnt=1

n=int(input("정수를 입력하세요 : "))
def is_prime_num(n):
    arr = [True] * (n + 1) # 특정 수가 지워졌는지 아닌지 확인하기 위한 배열

    for i in range(2, n + 1):
        if arr[i] == True: # 특정 수가 지워지지 않았다면 (소수여서)
            j = 2

            while (i * j) <= n:
                arr[i*j] = False # i의 배수의 값을 False로 지워준다.
                j += 1

    return arr


start_t=time.time()
for i in range(2, n):
    if(is_prime_num(i)==True):
        cnt+=1
end_t=time.time()
elapsed_t=end_t-start_t
print("{0}은 {1}번째 소수입니다.".format(n,cnt))
print(elapsed_t)
#%%

# 소수는 1과 자신을 나눠서 0인 나머지를 갖는 숫자다.