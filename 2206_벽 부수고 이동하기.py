import sys
import collections

def bfs(grid,n,m):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    queue = collections.deque()
    c = 0
    queue.append((c,0,0))
    count = 1
    distance = 1

    grid[0][0] = '2'
    while queue:
        c,x,y = queue.popleft()
        count-=1
        if x==n-1 and y==m-1:
            return distance
        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            if 0<=px<n and 0<=py<m:
                if c==0:
                    if grid[px][py]=='0' or grid[px][py]=='3':
                        grid[px][py] = '2'
                        queue.append((c,px,py))
                    elif grid[px][py]=='1':
                        queue.append((1,px,py))
                else:
                    if grid[px][py]=='0':
                        grid[px][py]= '3'
                        queue.append((c,px,py))

        if count==0:
            count = len(queue)
            distance+=1

    return -1


n,m = map(int,sys.stdin.readline().split())
grid = []
for _ in range(n):
    grid.append(list(sys.stdin.readline().rstrip()))
    
print(bfs(grid,n,m))