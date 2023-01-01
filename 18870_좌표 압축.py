import sys
import bisect

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))
sorted_list = sorted(set(n_list))

for i in n_list:
    print(bisect.bisect_left(sorted_list,i),end=' ')