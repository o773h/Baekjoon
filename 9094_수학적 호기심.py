import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())
    result = 0
    for b in range(1,n):
        for a in range(b+1,n):
            if (a**2+b**2+m) % (a*b) == 0:
                result+=1
    
    print(result)