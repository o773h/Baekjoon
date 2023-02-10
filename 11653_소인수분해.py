import sys

n = int(sys.stdin.readline())

for i in range(2,n+1):
    if n==1:
        break
    while n%i==0:
        print(i)
        n//=i