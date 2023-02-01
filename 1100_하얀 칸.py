import sys

grid1 = []
grid2 = []
for _ in range(4):
    grid1.append(list(sys.stdin.readline().strip()))
    grid2.append(list(sys.stdin.readline().strip()))

count = 0
for i in grid1:
    for j in range(0,8,2):
        if i[j]=='F':
            count+=1

for i in grid2:
    for j in range(1,8,2):
        if i[j]=='F':
            count+=1

print(count)