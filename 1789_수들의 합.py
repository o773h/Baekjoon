import sys

n = int(sys.stdin.readline())
sum = 0
if n==1:
    print(1)
for i in range(1,n+1):
    sum +=i
    if sum>n:
        print(i-1)
        break