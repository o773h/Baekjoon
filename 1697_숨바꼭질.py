import sys
import collections

def bfs(n_list,x):
    queue = collections.deque()
    queue.append(x)
    n_list[x]=1
    while queue:
        x = queue.popleft()
        px_list = {x+1,x-1,x*2}
        for px in px_list:
            if 0<=px<len(n_list):
                if n_list[px]==-1:
                    return n_list[x]
                elif n_list[px]==0:
                    n_list[px] = n_list[x]+1
                    queue.append(px)

n,k = map(int,sys.stdin.readline().split())

if n==k:
    print(0)
else:
    n_list = [0 for _ in range(100001)]
    n_list[k]=-1
    print(bfs(n_list,n))