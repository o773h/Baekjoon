import sys

n,s = map(int,sys.stdin.readline().split())
n_list = list(map(int,sys.stdin.readline().split()))

start = 0
end = 0
sum = 0

min_length = 0

while start<n:
    if sum>=s:
        if min_length==0:
            min_length=end-start
        else:
            if end-start>=min_length:
                sum -= n_list[start]
                start+=1
            else:
                min_length = end-start
    
    if sum<s:
        if end==n:
            break
        sum += n_list[end]
        end+=1


print(min_length)