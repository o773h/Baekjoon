import sys

n = int(sys.stdin.readline())

q = [0,0,0,0,0]

for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    if x>0:
        if y>0:
            q[1]+=1
        elif y<0:
            q[4]+=1
        else:
            q[0]+=1
    elif x<0:
        if y>0:
            q[2]+=1
        elif y<0:
            q[3]+=1
        else:
            q[0]+=1
    else:
        q[0]+=1

print("Q1:",q[1])
print("Q2:",q[2])
print("Q3:",q[3])
print("Q4:",q[4])
print("AXIS:",q[0])