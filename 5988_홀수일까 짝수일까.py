import sys

n = int(sys.stdin.readline())
for _ in range(n):
    k = int(sys.stdin.readline())
    if k%2==0:
        print("even")
    else:
        print("odd")