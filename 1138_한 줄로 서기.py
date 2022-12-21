import sys

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))
result_list = [0 for _ in range(n)]
i = 0
idx = 0
count = 0
while idx<n:

    if result_list[i]==0:
        if n_list[idx]==count:
            result_list[i]=(idx+1)
            idx+=1
            i=0
            count = 0
        else:
            count+=1
            i+=1
    else:
        i+=1
    if i>n-1:
        i=0

print(*result_list)