import sys
import collections

n,b,w = map(int,sys.stdin.readline().split())

road = sys.stdin.readline().rstrip()

queue = collections.deque()
wb_count = {'W':0, 'B':0}
result = 0

for i in road:
    if i=='B':
        wb_count[i]+=1
        queue.append(i)
        if wb_count[i]>b:
            if wb_count['W']>=w:
                result = max(result,sum(wb_count.values())-1)
            while wb_count['B']>b:
                wb_count[queue.popleft()]-=1
    else:
        wb_count[i]+=1
        queue.append(i)

if wb_count['W']>=w:
    result = max(result,sum(wb_count.values()))

print(result)