import sys

t = int(sys.stdin.readline())

for _ in range(t):
    l = list(map(int,sys.stdin.readline().split()))
    l.sort(reverse=True)
    print(l[2])