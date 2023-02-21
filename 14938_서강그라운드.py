import sys
import heapq

INF = int(1e9)

n,m,r = map(int,sys.stdin.readline().split())
t = [0]
t.extend(list(map(int,sys.stdin.readline().split())))

distance = [[INF for _ in range(n+1)] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for _ in range(r):
    a,b,l = map(int,sys.stdin.readline().split())
    graph[a].append((b,l))
    graph[b].append((a,l))


def dijkstra(start):
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start][start] = 0
    result = 0

    while queue:
        dist, node = heapq.heappop(queue)
        if dist > distance[start][node]:
            continue
        result+=t[node]

        for next in graph[node]:
            cost = dist + next[1]
            if cost < distance[start][next[0]]:
                if cost<=m:
                    distance[start][next[0]] = cost
                    heapq.heappush(queue,(cost,next[0]))
    return result


for i in range(1,n+1):
    result[i] = dijkstra(i)

print(max(result))