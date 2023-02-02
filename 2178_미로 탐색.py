import sys
import collections

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(x,y,grid):
    queue = collections.deque()
    queue.append((x,y))
    grid[x][y]='0'
    distance = 1
    count = 1

    while queue:
        x,y = queue.popleft()
        count-=1
        if x==n-1 and y==m-1:
            return distance
        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            if 0<=px<n and 0<=py<m:
                if grid[px][py]=='1':
                    grid[px][py]='0'
                    queue.append((px,py))

        if count==0:
            count = len(queue)
            distance+=1
    return distance

n,m = map(int,sys.stdin.readline().split())
grid = []
for _ in range(n):
    grid.append(list(sys.stdin.readline().rstrip()))

print(bfs(0,0,grid))