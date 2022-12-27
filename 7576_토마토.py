import sys
import collections

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(tomatoes,xy_list):
    queue = collections.deque()
    for i in xy_list:
        queue.append(i)

    days = 0
    count = len(queue)
    flag = False

    while queue:
        x,y = queue.popleft()
        count-=1
        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            if 0<=px<m and 0<=py<n:
                if tomatoes[py][px]==0:
                    tomatoes[py][px]=1
                    queue.append((px,py))
                    flag = True
        if count==0 and flag:
            if queue:
                count = len(queue)
                days+=1

    return days


m,n = map(int,sys.stdin.readline().split())

tomatoes = [[] for _ in range(n)]

for i in range(n):
    tomatoes[i] = list(map(int,sys.stdin.readline().split()))

xy_list = []
for j in range(m):
    for i in range(n):
        if tomatoes[i][j]==1:
            xy_list.append((j,i))

result = bfs(tomatoes,xy_list)

for j in range(m):
    for i in range(n):
        if tomatoes[i][j]==0:
            result = -1
            break

print(result)