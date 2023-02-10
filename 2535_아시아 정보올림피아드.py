import sys
import heapq

heap = []
n = int(sys.stdin.readline())
for _ in range(n):
    a,b,c = map(int,sys.stdin.readline().split())
    heapq.heappush(heap,(-c,a,b))

c,a,b = heapq.heappop(heap)
print(a,b)
c,a1,b = heapq.heappop(heap)
print(a1,b)

if a==a1:
    while True:
        c,a2,b = heapq.heappop(heap)
        if a2!=a:
            print(a2,b)
            break
else:
    c,a2,b = heapq.heappop(heap)
    print(a2,b)