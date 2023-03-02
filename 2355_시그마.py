import sys

a,b = map(int,sys.stdin.readline().split())
a,b = min(a,b),max(a,b)
print((a+b)*(b-a+1)//2)