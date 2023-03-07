import sys

a,b = map(int,sys.stdin.readline().split())

if a*(100-b)//100 <100:
    print(1)
else:
    print(0)