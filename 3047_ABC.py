import sys

n = list(map(int,sys.stdin.readline().split()))
n.sort()

s = sys.stdin.readline().rstrip()

for a in s:
    if a=='A':
        print(n[0],end=' ')
    elif a=='B':
        print(n[1],end=' ')
    else:
        print(n[2],end=' ')