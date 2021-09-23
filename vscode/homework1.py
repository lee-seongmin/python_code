#%%
gugudan_button='y'
while(gugudan_button=='y' or gugudan_button=='Y'):
    final_num=int(input("구구단을 계산하고 싶은 범위의 숫자를 정해주세요!!"))
    if(final_num>0):
        for i in range(1,final_num+1):
            for j in range(1,10):
                print(i*j, end=" ")
                if(j==9):
                    print("\n")
    else:
        print("숫자를 잘못입력하셨습니다.")
    gugudan_button=input("계속하려면 y나 Y를 입력하세요.")
    if(gugudan_button!='y' and gugudan_button!='Y'):
        break
#%%
x=int(input("첫번째 정수"))
y=int(input("두번째 정수"))
if(x > y):
    for i in range(1,x+1):
        if(x % i == 0 and y % i == 0):
            print("최대공약수={0}".format(y))
            break
if(x < y):
    for i in range(1,y+1):
        if(x % i == 0 and y % i == 0):
            print("최대공약수={0}".format(x))
            break
#%%
import math

bank_money=1000*(10**4)
isa=int(input("현재은행이율"))
mangee_money=2*bank_money
term=math.log(mangee_money / bank_money) / math.log(1+ isa / 100)
print(term) 

#%%
cnt = 0
for i in range(1,51):
    cnt+= (2*i-1) / (2*i+1)
print(cnt)
# %%
for i in range(1,11):
    print("{0} {1} {2} {3}".format(i**1, i**2, i**3, i**4))