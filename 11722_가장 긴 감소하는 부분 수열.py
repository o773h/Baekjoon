import sys
import bisect

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

a = a[::-1]
result = [a[0]]
for i in range(1,n):
    if result[-1]<a[i]:
        result.append(a[i])
    else:
        idx = bisect.bisect_left(result,a[i])
        result[idx] = a[i]

print(len(result))