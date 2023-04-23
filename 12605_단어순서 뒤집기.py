import sys

n = int(sys.stdin.readline())

for i in range(1,n+1):
    s_list = list(sys.stdin.readline().split())
    print("Case #{}: ".format(i),end='')
    print(*s_list[::-1])