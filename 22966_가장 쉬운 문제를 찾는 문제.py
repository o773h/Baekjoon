import sys

n = int(sys.stdin.readline())
difficulty = 5
for _ in range(n):
    a,b = sys.stdin.readline().split()
    if int(b)<difficulty:
        result = a
        difficulty = int(b)

print(result)