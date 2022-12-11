import sys

n = int(sys.stdin.readline())
xy_list=[]
for _ in range(n):
    xy_list.append(list(map(int,sys.stdin.readline().split())))

xy_list.sort(key=lambda x:(x[0],x[1]))

for lst in xy_list:
    print(lst[0],lst[1])