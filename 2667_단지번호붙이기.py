import sys
import collections

def bfs(grid,x,y):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    grid[x][y]='0'
    queue = collections.deque()
    queue.append((x,y))
    houses = 0

    while queue:
        x,y = queue.popleft()
        houses+=1
        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            if 0<=px<n and 0<=py<n:
                if grid[px][py]=='1':
                    grid[px][py]='0'
                    queue.append((px,py))
    return houses


n = int(sys.stdin.readline())
grid = []
for _ in range(n):
    grid.append(list(sys.stdin.readline().rstrip()))

house_list = []
count = 0
for i in range(n):
    for j in range(n):
        if grid[i][j]=='1':
            house_list.append(bfs(grid,i,j))
            count +=1
house_list.sort()

print(count)
if count!=0:
    print(*house_list,sep='\n')