import sys
n = int(sys.stdin.readline())
xy_list = []
for _ in range(n):
    xy_list.append(list(map(int,sys.stdin.readline().split())))
count = [1 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if xy_list[i][0]<xy_list[j][0]:
            if xy_list[i][1]<xy_list[j][1]:
                count[i]+=1

print(*count,sep=' ')