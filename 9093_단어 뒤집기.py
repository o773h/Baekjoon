import sys

t = int(sys.stdin.readline())

for _ in range(t):
    s_list = list(sys.stdin.readline().split())
    for s in s_list:
        print(s[::-1],end=' ')
    print()