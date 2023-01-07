import sys
import collections

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def bfs(grid,x,y,find):
    queue = collections.deque()
    queue.append((x,y))
    if find=='R':
        grid[y][x]='X'
    elif find=='G':
        grid[y][x]='X'
    else:
        grid[y][x]='Y'

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            px = x+dx[i]
            py = y+dy[i]
            if 0<=px<n and 0<=py<n:
                if find=='R' and grid[py][px]=='R':
                    grid[py][px]='X'
                    queue.append((px,py))
                elif find=='G' and grid[py][px]=='G':
                    grid[py][px]='X'
                    queue.append((px,py))
                elif find=='B' and grid[py][px]=='B':
                    grid[py][px]='Y'
                    queue.append((px,py))
                elif find=='X' and grid[py][px]=='X':
                    grid[py][px]='Y'
                    queue.append((px,py))

n = int(sys.stdin.readline())
grid=[]

for _ in range(n):
    grid.append(list(sys.stdin.readline().strip()))

count_r = 0
count_g = 0
count_b = 0
count_x = 0

for i in range(n):
    for j in range(n):
        if grid[i][j]=='R':
            bfs(grid,j,i,'R')
            count_r+=1
        elif grid[i][j]=='G':
            bfs(grid,j,i,'G')
            count_g+=1
        elif grid[i][j]=='B':
            bfs(grid,j,i,'B')
            count_b+=1


for i in range(n):
    for j in range(n):
        if grid[i][j]=='X':
            bfs(grid,j,i,'X')
            count_x+=1

print(count_r+count_b+count_g,count_x+count_b)