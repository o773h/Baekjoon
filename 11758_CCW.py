import sys

def ccw(p1,p2):
    if p1[0]*p2[1] - p2[0]*p1[1]>0:
        return 1
    elif p1[0]*p2[1] - p2[0]*p1[1]<0:
        return -1
    else:
        return 0


x1,y1 = map(int,sys.stdin.readline().split())
x2,y2 = map(int,sys.stdin.readline().split())
x3,y3 = map(int,sys.stdin.readline().split())

p1 = (x2-x1,y2-y1)
p2 = (x3-x1,y3-y1)

print(ccw(p1,p2))