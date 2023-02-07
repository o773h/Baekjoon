import sys
import heapq

INF = int(1e9)
BLACK = 3000
dx=[-1,0,1,0]
dy=[0,-1,0,1]

n = int(sys.stdin.readline())
grid = []
distance = [[INF for _ in range(n)] for _ in range(n)]


for _ in range(n):
    grid.append(list(sys.stdin.readline().strip()))

def dijkstra(grid,distance):
    queue = []
    heapq.heappush(queue,(0,(0,0)))
    distance[0][0] = 0

    while queue:
        dist, (x, y) = heapq.heappop(queue)
        if x==n-1 and y==n-1:
            return dist

        if dist > distance[x][y]:
            continue
        
        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            if 0<=px<n and 0<=py<n:
                if grid[px][py]=='0':
                    if dist+BLACK < distance[px][py]:
                        distance[px][py] = dist+BLACK
                        heapq.heappush(queue,(distance[px][py],(px,py)))
                else:
                    if dist+1 < distance[px][py]:
                        distance[px][py] = dist+1
                        heapq.heappush(queue,(distance[px][py],(px,py)))


print(dijkstra(grid,distance)//BLACK)