import sys

n,m = map(int,sys.stdin.readline().split())
a_list = list(map(int,sys.stdin.readline().split()))

start = 0
end = 0
sum = 0
count = 0

while start<n:
    if sum==m:
        count+=1

    if sum<m:
        if end==n:
            break
        sum+=a_list[end]
        end+=1
        
    else:
        sum-=a_list[start]
        start+=1

print(count)