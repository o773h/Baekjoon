import sys
import collections

a,b = map(int,sys.stdin.readline().split())

queue = collections.deque()
queue.extend([4,7])
count = 0

while queue:
    num = queue.popleft()
    if num<=a:
        queue.extend([num*10+4, num*10+7])
        if num==a:
            count+=1
    elif num<=b:
        count+=1
        if num<b:
            queue.extend([num*10+4, num*10+7])
    

print(count)