import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    max_num = 0
    max_univ = ''
    for _ in range(n):
        univ,num = sys.stdin.readline().split()
        if int(num) > max_num:
            max_num = int(num)
            max_univ = univ

    print(max_univ)