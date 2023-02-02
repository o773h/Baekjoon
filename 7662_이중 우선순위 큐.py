import sys
import heapq
from collections import defaultdict

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    min_heap = []
    max_heap = []
    count = 0
    max_delete_dict = defaultdict(int)
    min_delete_dict = defaultdict(int)
    for _ in range(k):
        s,n = sys.stdin.readline().split()
        if s=='D':
            if count==0:
                continue
            else:
                if n=='-1':
                    num = heapq.heappop(min_heap)
                    while -num in max_delete_dict:
                        max_delete_dict[-num]-=1
                        if max_delete_dict[-num]==0:
                            del max_delete_dict[-num]
                        num = heapq.heappop(min_heap)
                    min_delete_dict[num]+=1
                    
                    count-=1
                else:
                    num = heapq.heappop(max_heap)
                    while -num in min_delete_dict:
                        min_delete_dict[-num]-=1
                        if min_delete_dict[-num]==0:
                            del min_delete_dict[-num]
                        num = heapq.heappop(max_heap)
                    max_delete_dict[num]+=1
                    count-=1

        else:
            heapq.heappush(min_heap,int(n))
            heapq.heappush(max_heap,-int(n))
            count+=1

    if count==0:
        print("EMPTY")
    else:
        max_num = heapq.heappop(max_heap)
        while -max_num in min_delete_dict:
            min_delete_dict[-max_num]-=1
            if min_delete_dict[-max_num]==0:
                del min_delete_dict[-max_num]
            max_num = heapq.heappop(max_heap)

        min_num = heapq.heappop(min_heap)    
        while -min_num in max_delete_dict:
            max_delete_dict[-min_num]-=1
            if max_delete_dict[-min_num]==0:
                del max_delete_dict[-min_num]
            min_num = heapq.heappop(min_heap)

        print(-max_num,min_num)