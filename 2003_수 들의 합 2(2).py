import sys

n,m = map(int,sys.stdin.readline().split())
a_list = list(map(int,sys.stdin.readline().split()))


end = 0
sum = 0
count = 0

for start in range(n):

    while sum<m and end<n:
        sum+=a_list[end]
        end+=1

    if sum==m:
        count+=1
  
    sum-=a_list[start]


print(count)