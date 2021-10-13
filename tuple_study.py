my_variable = ()
print(type(my_variable))
#%%
movie_rank = ('닥터스트레인지','스플릿','럭키')
print(movie_rank)
# %%
num = (1)
print(type(num))
nums = (1,) #튜플로 하나를 선언하고 싶을 땐 콤마를 넣어줘야한다.
print(type(nums))
t = 1, 2, 3, 4 # 원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만, 
print(type(t)) # 사용자 편의를 위해 괄호 없이도 동작합니다.
# %%
tu = ('a', 'b', 'c')
t = ('A','b','c')
print(t)
q = tu[:1] + ('B',) + tu[2:]
print(q)
# %%
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(interest)
a=list(interest)
a[0]='현대로보틱스'
print(a)
b = tuple(a)
print(b)
# %%
tp = ()
for i in range(1,100):
    if(i%2==0):
        tp+=(i,)
print(tp)
# %%
