# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 16:01:57 2021

@author: pc03
"""

a=[1,2,3]
b=a
b[1]=0
print(b)
print(a)
# %%
import copy

a = [[1,2],[3,4],[5,6]]
b =copy.deepcopy(a)
id(a), id(b)

a[0][0]=4

print(a)
print(b)
#%%

def getGrade(score):
    if(score >= 95):
        print("성적은 A+입니다.")
    elif(score >= 90):
        print("성적은 A입니다.")
    elif(score >= 85):
        print("성적은 B+입니다.")
    elif(score >= 80):
        print("성적은 B입니다.")
    elif(score >= 75):
        print("성적은 c+입니다.")
    elif(score >=70):
        print("성적은 c입니다.")
    elif(score >=60):
        print("성적은 d입니다.")
    else:
        print("성적은 f입니다.")
test_score = int(input("점수를 입력하세요 :"))
getGrade(test_score)

#%%

# list에 값을 할당해서 for문을 돌려서 

#%%

#최대공약수를 어떻게 구할 것인가
#유클리드 알고리즘을 쓴다.
# a=36, b=12 r = a/b=3
# b=12 , r=3 k= b / r=4
# 안 나눠지는 수끼리 곱해서 답을 구한다.

def getGCD(a,b):
    gcd=1
    i=2
    while i<=a and i<=b:
        print(gcd)
#%%
#성적처리프로그램
score=[]
scoreSum=0
highScore=0
button='y'
def print_score(score):
    for i in range(0,len(score)):
        global scoreSum
        scoreSum+=score[i]
        
        if(score[i] >= 80):
            global highScore 
            highScore+= 1
    print("성적평균을 계산하세요 : {0}".format(scoreSum / len(score)))
    print("80점 이상 성적을 받은 학생은 {0}명입니다.".format(highScore))

while(button=='y' or button== 'Y'):
    print_score(score)
    student = int(input("성적을 입력하세요 : "))
        
    if(student > 0 and student <= 100):
        score.append(student)
    else:
        scoreSum=0
        highScore=0
        button = input("다시하겠습니까? 다시하려면 y나 Y를 입력하세요 ")
#%%
            
        
