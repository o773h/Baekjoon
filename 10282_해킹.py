import sys
import heapq

INF = int(1e9)

def dijkstra(start,distance,graph):
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start] = 0

    while queue:
        dist,node = heapq.heappop(queue)

        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = dist + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(queue,(cost,next[0]))
    return distance


t = int(sys.stdin.readline())

for _ in range(t):
    n,d,c = map(int,sys.stdin.readline().split())
    distance = [INF for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a,b,s = map(int,sys.stdin.readline().split())
        graph[b].append((a,s))

    distance = dijkstra(c,distance,graph)
    
    count = 0
    max_distance = 0
    for i in distance:
        if i!=INF:
            count+=1
            if i>max_distance:
                max_distance=i
    
    print(count, max_distance)