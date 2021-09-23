import sys
n=int(sys.stdin.readline())
if(n >= 1 and n <= 10000):
    for i in range(1,n+1):
        sum = 0
        sum += int((i * (i+1) / 2))
    print(sum)