import sys

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))

result = 0
idx = 0
for i in range(1,n):
    if n_list[i]>n_list[i-1]:
        if i==n-1:
            result = max(result,n_list[i]-n_list[idx])    
        continue
    else:
        result = max(result,n_list[i-1]-n_list[idx])
        idx = i

print(result)