import sys
from collections import defaultdict

n,d,k,c = map(int,sys.stdin.readline().split())
n_list = []
for _ in range(n):
    n_list.append(int(sys.stdin.readline()))

n_list.extend(n_list)
n_dict = defaultdict(int)

n_dict[c] = 1

for i in range(k):
    n_dict[n_list[i]]+=1


max_len = len(n_dict)

start = 0
end = k-1

while end<n+k:
    n_dict[n_list[start]]-=1
    if n_dict[n_list[start]]==0:
        del n_dict[n_list[start]]
    
    start+=1
    end+=1

    n_dict[n_list[end]]+=1
    
    max_len = max(max_len,len(n_dict))


print(max_len)