import sys

k = int(sys.stdin.readline())

a,b = 1,0

for _ in range(k):
    t = a
    a = b
    b = t+b

print(a,b)