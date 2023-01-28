import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n,m,k = map(int,sys.stdin.readline().split())
    n_list = list(map(int,sys.stdin.readline().split()))

    if n==m:
        if k>sum(n_list):
            print(1)
        else:
            print(0)
        continue

    start = 0
    end = m-1
    money_sum = sum(n_list[:m])
    count = 0
    while start<n:
        if money_sum<k:
            count+=1

        money_sum-=n_list[start]
        end+=1
        start+=1
        money_sum+=n_list[end%n]

    print(count)