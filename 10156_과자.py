import sys

k,n,m = map(int,sys.stdin.readline().split())
result = k*n-m if k*n-m>0 else 0

print(result)