import sys

a,b = map(int,sys.stdin.readline().split())
a,b = min(a,b),max(a,b)
if a==b:
    print(0)
else:
    print(b-a-1)
for i in range(a+1,b):
    print(i,end=' ')