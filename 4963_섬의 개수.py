import sys
import collections

dx = [1,1,1,-1,-1,-1,0,0]
dy = [0,-1,1,0,-1,1,-1,1]

def dfs(graph,y,x):

    queue = collections.deque()
    queue.append((y,x))
    graph[y][x]=0
    
    while queue:
        y,x = queue.popleft()
        for i in range(8):
            px = x+dx[i]
            py = y+dy[i]
            if 0<=px<w and 0<=py<h:
                if graph[py][px]==1:
                    graph[py][px]=0
                    queue.append((py,px))

while True:
    count = 0
    w,h = map(int,sys.stdin.readline().split())

    if w==0 and h==0:
        break

    graph = [[] for _ in range(h)]

    for i in range(h):
        graph[i] = list(map(int,sys.stdin.readline().split()))
    
    for i in range(w):
        for j in range(h):
            if graph[j][i]==1:
                dfs(graph,j,i)
                count+=1
    print(count)