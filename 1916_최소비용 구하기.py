import sys
import heapq

INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
    u,v,w, = map(int,sys.stdin.readline().split())
    graph[u].append((v,w))

start,end = map(int,sys.stdin.readline().split())

def dijkstra(start,end):
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start] = 0
    
    while queue:
        dist, node = heapq.heappop(queue)

        if node == end:
            return dist

        if dist > distance[node]:
            continue

        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue,(cost,i[0]))

print(dijkstra(start,end))