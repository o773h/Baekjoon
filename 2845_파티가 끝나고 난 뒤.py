import sys

l,p = map(int,sys.stdin.readline().split())

n = map(int,sys.stdin.readline().split())

for i in n:
    print(i - l*p,end=' ')