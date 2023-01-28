import sys

n,m = map(int,sys.stdin.readline().split())
n_list = list(map(int,sys.stdin.readline().split()))

end = 0
sum = 0
max_sum = 0
for start in range(n):
    while end<n and sum<m:
        sum+=n_list[end]
        end+=1

    if sum==m:
        max_sum = m
        break
    elif end==n and sum<m:
        max_sum = max(max_sum,sum)
        break
    else:
        max_sum = max(sum-n_list[end-1],max_sum)

    sum-=n_list[start]
    
print(max_sum)