import sys
import heapq

INF = int(1e9)

def dijkstra(start,end):
    distance = [INF for _ in range(v+1)]
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        if node==end:
            return dist

        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = dist + next[1]
            if distance[next[0]]>cost:
                distance[next[0]] = cost
                heapq.heappush(queue,(cost,next[0]))


v,e,p = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

if dijkstra(1,v) == (dijkstra(1,p) + dijkstra(p,v)):
    print("SAVE HIM")
else:
    print("GOOD BYE")