import sys
import collections

def topological_sort(n):
    queue = collections.deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            dp[i][i]=1
            queue.append(i)

    while queue:
        part = queue.popleft()

        for next in graph[part]:
            for i in range(1,n+1):
                dp[next[0]][i] += dp[part][i] * next[1]
                
            indegree[next[0]]-=1
            if indegree[next[0]]==0:
                queue.append(next[0])


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

for _ in range(m):
    x,y,k = map(int,sys.stdin.readline().split())
    graph[y].append((x,k))
    indegree[x]+=1

topological_sort(n)

for i in range(1,n+1):
    if dp[n][i]!=0:
        print(i,dp[n][i])