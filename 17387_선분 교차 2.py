import sys

def ccw(pa,pb):

    if pa[0]*pb[1] - pb[0] * pa[1]>0:
        return -1
    elif pa[0]*pb[1] - pb[0] * pa[1]<0:
        return 1
    else:
        return 0

x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
x3,y3,x4,y4 = map(int,sys.stdin.readline().split())



p1 = (x2-x1,y2-y1)
p2 = (x3-x1,y3-y1)
p3 = (x4-x1,y4-y1)

p4 = (x4-x3,y4-y3)
p5 = (x1-x3,y1-y3)
p6 = (x2-x3,y2-y3)

result1 = ccw(p1,p2) * ccw(p1,p3)
result2 = ccw(p4,p5) * ccw(p4,p6)

if result1 == -1:
    if result2 == 0 or result2 == -1:
        print(1)
    else:
        print(0)
elif result1 == 0:
    if result2 == -1:
        print(1)
    elif result2 == 0:
        if (min(x1,x2)<=x3<=max(x1,x2) and min(y1,y2)<=y3<=max(y1,y2)) or\
             (min(x1,x2)<=x4<=max(x1,x2) and min(y1,y2)<=y4<=max(y1,y2)) or \
                (min(x3,x4)<=x1<=max(x3,x4) and min(y3,y4)<=y1<=max(y3,y4)) or \
                    (min(x3,x4)<=x2<=max(x3,x4) and min(y3,y4)<=y2<=max(y3,y4)):
            print(1)
        else:
            print(0)
    else:
        print(0)
else:
    print(0)