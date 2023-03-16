import sys
import collections

def topological_sort():
    queue =collections.deque()
    queue.append((0,1))

    while queue:
        dist,node = queue.popleft()

        for next,r in graph[node]:
            if score[next]< r+dist:
                score[next] = r+dist
                parent[next] = node
            
            indegree[next]-=1
            if indegree[next] ==0:
                if next==1:
                    return
                queue.append((score[next],next))


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
parent = [i for i in range(n+1)]
score = [0 for _ in range(n+1)]
for _ in range(m):
    p,q,r = map(int,sys.stdin.readline().split())
    graph[p].append((q,r))
    indegree[q]+=1

topological_sort()

result = [1]
p = parent[1]
while p!=1:
    result.append(p)
    p = parent[p]
result.append(1)

print(score[1])
print(*result[::-1])