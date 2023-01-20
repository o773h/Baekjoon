import sys
import bisect

n, m = map(int,sys.stdin.readline().split())
n_list = []
for _ in range(n):
    n_list.append(int(sys.stdin.readline()))

n_list.sort()
diff = 2*n_list[-1]

for start in range(n):

    idx = bisect.bisect_left(n_list,m+n_list[start])    
    if idx==n:
        continue
 
    diff = min(diff,n_list[idx] - n_list[start])
    if diff==m:
        break


print(diff)