import sys

n = int(sys.stdin.readline())

if n%2==0:
    result = (n//2 +1)**2
else:
    n = (n+1)//2
    result = n * (n+1)

print(result)