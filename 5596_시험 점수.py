import sys

l1 = list(map(int,sys.stdin.readline().split()))
l2 = list(map(int,sys.stdin.readline().split()))

s1 = sum(l1)
s2 = sum(l2)
if s1 >= s2:
    print(s1)
else:
    print(s2)