import sys
import collections

def bfs(a,b):
    queue = collections.deque()
    queue.append(a)
    count = 1
    result = 1
    while queue:
        num = queue.popleft()
        count-=1

        num1 = num*2
        num2 = num*10 + 1

        if num1 == b or num2 == b:
            return result+1
        
        if num1<b:
            queue.append(num1)
        if num2<b:
            queue.append(num2)

        if count==0:
            count = len(queue)
            result+=1
    return -1
    
a,b = map(int,sys.stdin.readline().split())

print(bfs(a,b))