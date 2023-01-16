import sys

def ccw(pa,pb):

    if pa[0]*pb[1] - pb[0] * pa[1]>0:
        return -1
    else:
        return 1

x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
x3,y3,x4,y4 = map(int,sys.stdin.readline().split())

p1 = (x2-x1,y2-y1)
p2 = (x3-x1,y3-y1)
p3 = (x4-x1,y4-y1)

p4 = (x4-x3,y4-y3)
p5 = (x1-x3,y1-y3)
p6 = (x2-x3,y2-y3)

if (ccw(p1,p2) * ccw(p1,p3))==-1 and (ccw(p4,p5) *ccw(p4,p6)) ==-1:
    print(1)
else:
    print(0)
