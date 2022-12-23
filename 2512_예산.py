import sys

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())

n_list.sort()
start = 0
end = n_list[-1]

if sum(n_list)<=m:
    print(n_list[-1])
else:
    while start<end:
        mid = (start+end)//2
        sum = 0
        for i in n_list:
            if i<=mid:
                sum+=i
            else:
                sum+=mid
        if sum>m:
            end = mid
        else:
            start = mid+1

    print(start-1)