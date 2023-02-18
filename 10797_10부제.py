import sys

n = int(sys.stdin.readline())

cars=map(int,sys.stdin.readline().split())
result = 0
for i in cars:
    if i==n:
        result+=1

print(result)