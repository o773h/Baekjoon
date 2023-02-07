import sys
import collections

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs(grid,xyz):
    queue = collections.deque()
    queue.extend(xyz)
    count = len(queue)
    days = -1
    while queue:
        x,y,z = queue.popleft()
        count-=1
        for i in range(6):
            px = x + dx[i]
            py = y + dy[i]
            pz = z + dz[i]
            if 0<=px<h and 0<=py<m and 0<=pz<n:
                if grid[px][py][pz]==0:
                    grid[px][py][pz]=1
                    queue.append((px,py,pz))
        if count==0:
            count = len(queue)
            days+=1
    return days
            

n,m,h = map(int,sys.stdin.readline().split())
grid= []

for i in range(h):
    grid.append([])
    for _ in range(m):
        grid[i].append(list(map(int,sys.stdin.readline().split())))

xyz = []
for i in range(h):
    for j in range(m):
        for k in range(n):
            if grid[i][j][k]==1:
                xyz.append((i,j,k))

result = bfs(grid,xyz)

for i in range(h):
    for j in range(m):
        for k in range(n):
            if grid[i][j][k]==0:
                result = -1
                break

print(result)