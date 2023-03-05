import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    sum = 0
    for i in range(1,n+1,2):
        sum+=i
    print(sum)