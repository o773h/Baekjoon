import sys

m = int(sys.stdin.readline())

result = 1
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    if x==result:
        result = y
    elif y==result:
        result = x

print(result)