import sys
import heapq

n,k = map(int,sys.stdin.readline().split())
jewels = []
for _ in range(n):
    m,v = map(int,sys.stdin.readline().split())
    heapq.heappush(jewels,(m,v))

bag = []
for _ in range(k):
    bag.append(int(sys.stdin.readline()))

bag.sort()

curr_jewels = []
result = 0
for b in bag:
    while jewels and b>=jewels[0][0]:
        heapq.heappush(curr_jewels,(-heapq.heappop(jewels)[1]))
    
    if curr_jewels:
        result+= (-heapq.heappop(curr_jewels))

print(result)