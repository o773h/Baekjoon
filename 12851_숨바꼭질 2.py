import sys
import collections

def bfs(n,k):
    queue = collections.deque()
    queue.append(n)

    count = 1
    second = 0

    while queue:
        num = queue.popleft()
        count -=1
        n1 = num-1
        n2 = num+1
        n3 = 2*num

        if 0<=n1<=100000:
            if distance[n1]==-1 or distance[n1]==second:
                move(queue,n1,num,second)
        if 0<=n2<=100000:
            if distance[n2]==-1 or distance[n2]==second:
                move(queue,n2,num,second)
        if 0<=n3<=100000:
            if distance[n3]==-1 or distance[n3]==second:
                move(queue,n3,num,second)

        if count==0:
            count = len(queue)
            second+=1
            if cases[k]!=0:
                return distance[k]+1,cases[k]
            
def move(queue,n,num,second):
    cases[n]+=1
    distance[n] = second
    queue.append(n)


distance = [-1 for _ in range(100000+1)]
cases = [0 for _ in range(100000+1)]
n,k = map(int,sys.stdin.readline().split())
if n>=k:
    print(n-k)
    print(1)
else:
    print(*bfs(n,k),sep='\n')