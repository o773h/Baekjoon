import sys

a,b = map(int,sys.stdin.readline().split())
a = b-a

for i in range(10,1,-1):
    if a%i==0 and b%i==0:
        a//=i
        b//=i

print(a,b)