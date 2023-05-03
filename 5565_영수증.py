import sys

price = int(sys.stdin.readline())
n = 0
for _ in range(9):
    n += int(sys.stdin.readline())

print(price-n)