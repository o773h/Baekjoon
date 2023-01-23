import sys
import collections

dx = [-1,0,1,0]
dy = [0,-1,0,1]
grid = []

count = 0
area = 0

def bfs(x,y):
    area = 0
    queue = collections.deque()
    queue.append((x,y))
    grid[x][y]='0'
    while queue:
        x,y = queue.popleft()
        area +=1
        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            if 0<=px<n and 0<=py<m:
                if grid[px][py]=='1':
                    grid[px][py]='0'
                    queue.append((px,py))

    return area


n,m = map(int,sys.stdin.readline().split())
for _ in range(n):
    grid.append(list(sys.stdin.readline().split()))

for i in range(n):
    for j in range(m):
        if grid[i][j]=='1':
            count+=1
            area = max(area,bfs(i,j))

print(count)
print(area)