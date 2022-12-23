import sys

n,m = map(int,sys.stdin.readline().split())
n_list = list(map(int,sys.stdin.readline().split()))

start = max(n_list)
end = sum(n_list)

while start<end:
    lst = []
    sum = 0
    mid = (start+end)//2

    for i in n_list:
        sum+=i
        if sum>mid:
            lst.append(sum-i)
            sum = i

    lst.append(sum)

    if len(lst)<=m:
        end=mid
    else:
        start=mid+1

print(start)