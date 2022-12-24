import sys
import collections

dx = [-1,0,1,0]
dy = [0,1,0,-1]

t = int(sys.stdin.readline())

for _ in range(t):
    m,n,k = map(int,sys.stdin.readline().split())
    graph=[[0 for _ in range(n)] for _ in range(m)]
    count = 0

    for _ in range(k):
        x1,y1 = map(int,sys.stdin.readline().split())
        graph[x1][y1]=1

    def bfs(graph,x,y):

        graph[x][y] = 0
        queue = collections.deque()
        queue.append((x,y))

        while queue:
            x,y = queue.popleft()
            for i in range(4):
                px = x + dx[i]
                py = y + dy[i]
                if 0<=px<m and 0<=py<n:
                    if graph[px][py] == 1:
                        graph[px][py]=0
                        queue.append((px,py))

    for i in range(m):
        for j in range(n):
            if graph[i][j]==1:
                bfs(graph,i,j)
                count+=1

    print(count)