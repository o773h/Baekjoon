import sys

n = int(sys.stdin.readline())

result = 0
for i in range(1,n):
    result += n*i + i

print(result)