import sys

n = int(sys.stdin.readline())
s = set(map(int,sys.stdin.readline().split()))
l = list(s)
l.sort()
print(*l)