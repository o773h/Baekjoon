import sys

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))

n_list.sort()
result = 0

for i in range(n):
    start = 0
    end = n-1
    if start==i:
        start+=1
    elif end==i:
        end-=1
        
    while start<end:
        sum = n_list[start] + n_list[end]
        if sum==n_list[i]:
            result+=1
            break
        elif sum>n_list[i]:
            end-=1
            if end==i:
                end-=1
        else:
            start+=1
            if start==i:
                start+=1

print(result)