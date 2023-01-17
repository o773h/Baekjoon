import sys

def ccw(pa,pb,pc):
    if pa[0] * pb[1] - pb[0] * pa[1] > 0:
        result1 = -1
    elif pa[0] * pb[1] - pb[0] * pa[1] < 0:
        result1 = 1
    else:
        result1 = 0
    
    if pa[0] * pc[1] - pc[0] * pa[1] > 0:
        result2 = -1
    elif pa[0] * pc[1] - pc[0] * pa[1] < 0:
        result2 = 1
    else:
        result2 = 0

    return result1*result2

def check(xy1,xy2,xy3,xy4):
    if min(xy1[0],xy2[0])<=xy3[0]<=max(xy1[0],xy2[0]) and min(xy1[1],xy2[1])<=xy3[1]<=max(xy1[1],xy2[1]) or \
        min(xy1[0],xy2[0])<=xy4[0]<=max(xy1[0],xy2[0]) and min(xy1[1],xy2[1])<=xy4[1]<=max(xy1[1],xy2[1]) or \
        min(xy3[0],xy3[0])<=xy1[0]<=max(xy3[0],xy3[0]) and min(xy3[1],xy4[1])<=xy1[1]<=max(xy3[1],xy4[1]) or \
        min(xy3[0],xy3[0])<=xy2[0]<=max(xy3[0],xy3[0]) and min(xy3[1],xy4[1])<=xy2[1]<=max(xy3[1],xy4[1]):
        return True
    else:
        return False
        

t = int(sys.stdin.readline())

for _ in range(t):
    x_start,y_start,x_end,y_end,x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    xy_list = [[x1,y1],[x1,y2],[x2,y2],[x2,y1]]

    p = [x_end - x_start, y_end - y_start]
    
    p_list=[]
    for i in range(4):
        p_list.append([xy_list[i][0] - x_start, xy_list[i][1] - y_start])


    flag = False
    if min(x1,x2)<=min(x_start,x_end) and max(x_start,x_end)<=max(x1,x2) and \
        min(y1,y2)<=min(y_start,y_end) and max(y_start,y_end)<=max(y1,y2):
        flag = True

    else:
        for i in range(4):
            ans = ccw(p,p_list[i-1],p_list[i])
            if ans==-1:
                p1 = [xy_list[i][0]-xy_list[i-1][0],xy_list[i][1]-xy_list[i-1][1]]
                p2 = [x_start - xy_list[i-1][0],y_start - xy_list[i-1][1]]
                p3 = [x_end - xy_list[i-1][0],y_end - xy_list[i-1][1]]
                if ccw(p1,p2,p3)==-1:
                    flag = True
                    break
            elif ans==0:
                if check([x_start,y_start],[x_end,y_end],xy_list[i-1],xy_list[i]):
                    flag = True
                    break

    if flag:
        print("T")
    else:
        print("F")