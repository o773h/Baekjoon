import sys
import heapq

heap = []

n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline())
    if x==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(abs(x),x))