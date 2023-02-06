import sys
import heapq

INF = int(1e9)

v,e = map(int,sys.stdin.readline().split())
k = int(sys.stdin.readline())

graph = [[] for _ in range(v+1)]
distance = [INF for _ in range(v+1)]

for _ in range(e):
    a,b,w = map(int,sys.stdin.readline().split())
    graph[a].append((b,w))


def dijkstra(start):
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node]<dist:
            continue

        for i in graph[node]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue,(cost,i[0]))

dijkstra(k)

for i in range(1,v+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])