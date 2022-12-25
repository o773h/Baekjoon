import sys
import collections

dx = [-1,0,1,0]
dy = [0,-1,0,1]

t = int(sys.stdin.readline())

for _ in range(t):
    count = 0
    h,w = map(int,sys.stdin.readline().split())
    grid = [[] for _ in range(h)]

    for i in range(h):
        grid[i] = list(sys.stdin.readline().strip())
    
    def bfs(grid,x,y):
        queue = collections.deque()
        queue.append((x,y))
        
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                px = x+dx[i]
                py = y+dy[i]
                if 0<=px<w and 0<=py<h:
                    if grid[py][px]=='#':
                        queue.append((px,py))
                        grid[py][px]='.'
    
    for j in range(h):
        for i in range(w):
            if grid[j][i]=='#':
                bfs(grid,i,j)
                count+=1
    print(count)