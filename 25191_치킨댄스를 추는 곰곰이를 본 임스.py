import sys

n = int(sys.stdin.readline())
a,b = map(int,sys.stdin.readline().split())

result = a//2 + b
if result>n:
    print(n)
else:
    print(result)