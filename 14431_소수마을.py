import sys
import math
import heapq

INF = int(1e9)
def dijkstra():
    queue = []
    distance[0] = 0
    heapq.heappush(queue,(0,0))

    while queue:
        dist,node = heapq.heappop(queue)

        if node == 1:
            return dist

        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = dist + next[1]
            if distance[next[0]] > cost:
                distance[next[0]] = cost
                heapq.heappush(queue,(cost,next[0]))

    return -1


num = [True for _ in range(9000)]
prime_numbers=set()
for i in range(2,9000):
    if num[i]==True:
        prime_numbers.add(i)
        for j in range(i,9000,i):
            num[j]=False

x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+2)]
distance = [INF for _ in range(n+2)]
town = [(x1,y1),(x2,y2)]
for _ in range(n):
    town.append(tuple(map(int,sys.stdin.readline().split())))

for i in range(n+2):
    for j in range(i+1,n+2):
        dist = int(math.dist(town[i],town[j]))
        if dist in prime_numbers:
            graph[i].append((j,dist))
            graph[j].append((i,dist))

print(dijkstra())