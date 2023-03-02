import sys

is_arithmetic = False
is_geometric = False

n = int(sys.stdin.readline())

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if (b-a) == (c-b):
    is_arithmetic=True
else:
    is_geometric = True

num = c
for _ in range(n-3):
    num = int(sys.stdin.readline())

if is_arithmetic:
    print(num + (b-a))
else:
    print(num * (b//a))
