import sys
import heapq

INF = int(1e9)

def dijkstra(start):
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start][start] = 0

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[start][node] < dist:
            continue

        for next in graph[node]:
            cost = dist + 1
            if cost < distance[start][next]:
                distance[start][next] = cost
                heapq.heappush(queue,(cost,next))
    

n,k = map(int,sys.stdin.readline().split())

distance = [[INF for _ in range(n+1)] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(k):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)

for i in range(1,n+1):
    dijkstra(i)

s = int(sys.stdin.readline())
for _ in range(s):
    a,b = map(int,sys.stdin.readline().split())
    if distance[a][b]!=INF:
        print(-1)
    elif distance[b][a]!=INF:
        print(1)
    else:
        print(0)