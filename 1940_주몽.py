import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

n_list = list(map(int,sys.stdin.readline().split()))
n_list.sort()

start = 0
end = n-1
count = 0

while start<end:
    sum = n_list[start]+n_list[end]
    if sum==m:
        count+=1

    elif sum>m:
        end-=1
    
    if sum<=m:
        start+=1
        
print(count)