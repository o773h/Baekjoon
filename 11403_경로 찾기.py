import sys
import collections

def find_route(start):
    route = [0 for _ in range(n)]
    queue = collections.deque()
    queue.append(start)

    while queue:
        node = queue.popleft()

        for next in graph[node]:
            if route[next]==0:
                route[next] = 1
                queue.append(next)
            
    return route


n = int(sys.stdin.readline())
graph = [[] for _ in range(n)]

for a in range(n):
    m = map(int,sys.stdin.readline().split())
    for b,c in enumerate(m):
        if c==1:
            graph[a].append(b)

for i in range(n):
    print(*find_route(i))