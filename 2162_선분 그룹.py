import sys

def ccw(p1,p2):
    if p1[0]*p2[1] - p1[1]*p2[0]>0:
        return 1
    elif p1[0]*p2[1] - p1[1]*p2[0]<0:
        return -1
    else:
        return 0
    
def check_lines(i,j):
    x1,y1,x2,y2 = lines[i][0][0],lines[i][0][1],lines[i][1][0],lines[i][1][1]
    x3,y3,x4,y4 = lines[j][0][0],lines[j][0][1],lines[j][1][0],lines[j][1][1]

    p1 = (x2 - x1,y2 - y1)
    p2 = (x3 - x1,y3 - y1)
    p3 = (x4 - x1,y4 - y1)

    p4 = (x4 - x3,y4 - y3)
    p5 = (x1 - x3,y1 - y3)
    p6 = (x2 - x3,y2 - y3)

    if ccw(p1,p2)*ccw(p1,p3)==0:
        if ccw(p4,p5)*ccw(p4,p6)==0:
            if (x1==x3 and y1==y3) or (x1==x4 and y1==y4) or (x2==x3 and y2==y3) or (x2==x4 and y2==y4):
                return True
            elif (min(x1,x2)<=min(x3,x4)<=max(x1,x2) and min(y1,y2)<=min(y3,y4)<=max(y1,y2)) or\
            (min(x3,x4)<=min(x1,x2)<=max(x3,x4) and min(y3,y4)<=min(y1,y2)<=max(y3,y4)):
                return True
            else:
                return False
        elif ccw(p4,p5)*ccw(p4,p6)==-1:
            return True
        else:
            return False
    elif ccw(p4,p5)*ccw(p4,p6)==0:
        if ccw(p1,p2)*ccw(p1,p3)==-1:
            return True
        else:
            return False
    elif ccw(p1,p2)*ccw(p1,p3) ==-1 and ccw(p4,p5)*ccw(p4,p6)==-1:
        return True
    else:
        return False

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        size[a]+=size[parent[b]]
        parent[b] = a
        return 1
    elif a>b:
        size[b]+=size[parent[a]]
        parent[a] = b
        return 1
    return 0


n = int(sys.stdin.readline())   

lines = []
parent = [i for i in range(n)]
size = [1 for _ in range(n)]
set_num = n
for _ in range(n):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    lines.append(((x1,y1),(x2,y2)))

for i in range(n):
    for j in range(i+1,n):
        if find_parent(parent,i)!=find_parent(parent,j):
            if check_lines(i,j):
                set_num -= union_parent(parent,i,j)


print(set_num)
print(max(size))