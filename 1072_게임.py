import sys

x,y = map(int,sys.stdin.readline().split())

start = 0
end = x
z = y*100//x

if z>=99:
    print(-1)
else:
    while start < end:
        mid = (start + end) //2
        if z<((mid+y)*100)//(mid+x):
            end = mid
        else:
            start = mid+1
    print(start)