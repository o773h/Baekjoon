import sys
import heapq

INF = int(1e9)

n,m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
    a,b,w = map(int,sys.stdin.readline().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

def dijkstra(start,end):
    queue =[]
    heapq.heappush(queue,(0,start))
    distance[start] = 0

    while queue:
        dist,node = heapq.heappop(queue)

        if node==end:
            return dist

        if dist>distance[node]:
            continue

        for next_node in graph[node]:
            cost = dist+next_node[1]
            if cost < distance[next_node[0]]:
                distance[next_node[0]] = cost
                heapq.heappush(queue,(cost, next_node[0]))

print(dijkstra(1,n))