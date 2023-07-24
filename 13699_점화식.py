import sys

n = int(sys.stdin.readline())

t = [0 for _ in range(36)]
t[0] = 1
t[1] = 1

for i in range(2,n+1):
    for j in range(i):
        t[i] += t[j] * t[i-1-j]

print(t[n])