import sys

n,m = sys.stdin.readline().split()
m = int(m)
result = n*int(n)

if len(result)>m:
    print(result[:m])
else:
    print(result)