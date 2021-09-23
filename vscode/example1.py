x=int(input("첫번째 정수"))
y=int(input("두번째 정수"))
list_num=[]
if(x > y):
    for i in range(1,y+1):
        if(x % i == 0 and y % i == 0):
            list_num.append(i)
else:
    for i in range(1,x+1):
        if(x % i == 0 and y % i == 0):
            list_num.append(i)
print("최대공약수={0}".format(list_num.pop()))    