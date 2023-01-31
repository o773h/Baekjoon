import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    heapq.heappush(heap,int(sys.stdin.readline()))

result = 0
while len(heap)>=2:
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    sum = num1+num2
    heapq.heappush(heap,sum)
    result+=sum

print(result)