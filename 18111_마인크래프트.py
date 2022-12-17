import sys
import copy

n,m,b = map(int,sys.stdin.readline().split())
xy_list = []
for _ in range(n):
    xy_list.extend(list(map(int,sys.stdin.readline().split())))

min_height = min(xy_list)
max_height = max(xy_list)
min_time = 0
height = 0
flag = True

for i in range(min_height,max_height+1):
    box = b
    time = 0
    new_list = xy_list[:]
    for k in new_list:
        if k<i:
            box-=(i-k)
            time+=(i-k)
            k+=(i-k)
        elif k>i:
            box+=(k-i)
            time+= (2*(k-i))
            k-=(k-i)

    if box>=0:
        if flag:
            min_time = time
            height = i
            flag = False
        else:
            if min_time>=time:
                min_time = time
                height = i

print(min_time,height)