import sys

def check(x,y,cx,cy,r):
    if (x-cx)**2 + (y-cy)**2<r**2:
        return True
    else:
        return False

t = int(sys.stdin.readline())

for _ in range(t):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    count = 0
    for _ in range(n):
        x,y,r = map(int,sys.stdin.readline().split())
        check1 = check(x1,y1,x,y,r)
        check2 = check(x2,y2,x,y,r)
        if check1 or check2:
            if check1 and check2:
                continue
            count+=1
    
    print(count)