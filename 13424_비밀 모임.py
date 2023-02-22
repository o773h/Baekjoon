import sys
import heapq

INF = int(1e9)

def dijkstra(start,distance,graph):
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start][start]=0

    while queue:
        dist, node = heapq.heappop(queue)
        if dist > distance[start][node]:
            continue
        
        for next in graph[node]:
            cost = dist + next[1]
            if cost < distance[start][next[0]]:
                distance[start][next[0]] = cost
                heapq.heappush(queue,(cost,next[0]))


t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    distance = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,sys.stdin.readline().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    k = int(sys.stdin.readline())
    k_list = list(map(int,sys.stdin.readline().split()))
    
    for i in range(1,n+1):
        dijkstra(i,distance,graph)

    min_distance = INF
    result = 0
    for i in range(1,n+1):
        total_distacne = 0
        for j in k_list:
            total_distacne += distance[i][j]
        if total_distacne<min_distance:
            min_distance = total_distacne
            result = i
    
    print(result)