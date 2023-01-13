import sys
import collections

dx=[-1,0,1,0]
dy=[0,-1,0,1]

h,w = map(int,sys.stdin.readline().split())
grid = []
for _ in range(h):
    grid.append(list(sys.stdin.readline().strip()))

def bfs(grid,x,y,visited):
    queue = collections.deque()
    queue.append((x,y))
    visited[x][y]=1
    hour = 0
    count = 1

    while queue:
        x,y = queue.popleft()
        count -=1

        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            if 0<=px<h and 0<=py<w:
                if grid[px][py]=='L' and visited[px][py]==0:
                    visited[px][py]=1
                    queue.append((px,py))

        if count==0 and queue:
            hour+=1
            count = len(queue)
    return hour
        
max_hour = 0
for i in range(h):
    for j in range(w):
        if grid[i][j]=='L':
            if 1<=i<h-1 and 1<=j<w-1:
                if grid[i][j-1]=='L' and grid[i][j+1]=='L':
                    continue
                if grid[i+1][j]=='L' or grid[i+1][j]=='L':
                    continue
            visited=[[0] * w for _ in range(h)]
            max_hour = max(max_hour,bfs(grid,i,j,visited))


print(max_hour)