import sys
import heapq

dx = [-1,0,1,0]
dy = [0,-1,0,1]
INF = int(1e9)

def dijkstra(distance,grid,n):
    queue = []
    heapq.heappush(queue,(grid[0][0],(0,0)))
    distance[0][0] = grid[0][0]

    while queue:
        dist,(x,y) = heapq.heappop(queue)
        if x==n-1 and y==n-1:
            return dist
        if dist > distance[x][y]:
            continue

        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            if 0<=px<n and 0<=py<n:
                cost = dist + grid[px][py]
                if cost < distance[px][py]:
                    distance[px][py] = cost
                    heapq.heappush(queue,(cost,(px,py)))

result = []

while True:
    n = int(sys.stdin.readline())
    if n==0:
        break

    grid = []
    for _ in range(n):
        grid.append(list(map(int,sys.stdin.readline().split())))

    distance=[[INF for _ in range(n)] for _ in range(n)]  

    result.append(dijkstra(distance,grid,n))

for i in range(len(result)):
    print("Problem ",i+1,": ",result[i],sep='')