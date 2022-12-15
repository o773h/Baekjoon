import sys

xy_list = []
for _ in range(3):
    xy_list.append(list(map(int,sys.stdin.readline().split())))


if xy_list[0][0]==xy_list[1][0]:
    x = xy_list[2][0]
elif xy_list[0][0]==xy_list[2][0]:
    x = xy_list[1][0]
else:
    x = xy_list[0][0]

if xy_list[0][1]==xy_list[1][1]:
    y = xy_list[2][1]
elif xy_list[0][1]==xy_list[2][1]:
    y = xy_list[1][1]
else:
    y = xy_list[0][1]

print(x,y)