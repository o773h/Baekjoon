import sys
import bisect

t = int(sys.stdin.readline())

for _ in range(t):
    a,b = map(int,sys.stdin.readline().split())
    a_list = list(map(int,sys.stdin.readline().split()))
    b_list = list(map(int,sys.stdin.readline().split()))

    b_list.sort()
    sum = 0

    for i in a_list:
        sum+=bisect.bisect_left(b_list,i)
    print(sum)
