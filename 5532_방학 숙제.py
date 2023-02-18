import sys

l = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())

if a%c==0:
    a_days = a//c
else:
    a_days = a//c +1

if b%d==0:
    b_days = b//d
else:
    b_days = b//d +1

print(l - max(a_days,b_days))