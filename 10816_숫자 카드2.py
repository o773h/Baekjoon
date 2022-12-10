import sys
import bisect

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int,sys.stdin.readline().split()))

n_list.sort()

for i in m_list:
    print(bisect.bisect_right(n_list,i)-bisect.bisect_left(n_list,i),end=' ')