import sys

n,m = map(int,sys.stdin.readline().split())
ball = [i for i in range(1,n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    ball[a-1],ball[b-1] = ball[b-1],ball[a-1]

print(*ball)