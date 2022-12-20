import sys
import math

xy = list(map(int,sys.stdin.readline().split()))
flag = True
if xy[0]==xy[2]==xy[4]:
    flag = False
elif xy[4]==xy[2]:
    if (xy[1]-xy[3])/(xy[0]-xy[2]) == (xy[1]-xy[5])/(xy[0]-xy[4]):
        flag = False
elif xy[0]==xy[2]:
    if (xy[3]-xy[5])/(xy[2]-xy[4]) == (xy[1]-xy[5])/(xy[0]-xy[4]):
        flag = False
elif xy[0]==xy[4]:
    if (xy[1]-xy[3])/(xy[0]-xy[2]) == (xy[3]-xy[5])/(xy[2]-xy[4]):
        flag = False
else:
    if (xy[1]-xy[3])/(xy[0]-xy[2]) == (xy[1]-xy[5])/(xy[0]-xy[4]):
        flag = False

if flag:
    len1 = math.sqrt((xy[0]-xy[2])**2 + (xy[1]-xy[3])**2)
    len2 = math.sqrt((xy[0]-xy[4])**2 + (xy[1]-xy[5])**2)
    len3 = math.sqrt((xy[4]-xy[2])**2 + (xy[5]-xy[3])**2)

    sum = len1+len2+len3
    max_len = sum - min(len1,len2,len3)
    min_len = sum - max(len1,len2,len3)

    result = (max_len -min_len) * 2
    print(result)
else:
    print(-1.0)