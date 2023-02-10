import sys

t = int(sys.stdin.readline())
for _ in range(t):
    sum_a = 0
    sum_b = 0
    for _ in range(9):
        a,b = map(int,sys.stdin.readline().split())
        sum_a += a
        sum_b += b

    if sum_a>sum_b:
        print("Yonsei")
    elif sum_a<sum_b:
        print("Korea")
    else:
        print("Draw")