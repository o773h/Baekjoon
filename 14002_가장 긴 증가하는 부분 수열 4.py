import sys
import bisect

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

lis = [a[0]]
result = [0]
for i in range(1,n):
    if lis[-1]<a[i]:
        lis.append(a[i])
        result.append(len(lis)-1)
    else:
        idx = bisect.bisect_left(lis,a[i])
        lis[idx] = a[i]
        result.append(idx)

res = []
l = len(lis)-1
for i in range(n-1,-1,-1):
    if result[i] == l:
        res.append(a[i])
        l-=1
    if l<0:
        break

print(len(lis))
print(*res[::-1])