import sys

num = int(sys.stdin.readline())

for _ in range(num):
    n,m = map(int,sys.stdin.readline().split())
    n_list = list(map(int,sys.stdin.readline().split()))
    count = 0
    last_idx=0

    for i in range(max(n_list),n_list[m],-1):
        newlast_idx = last_idx
        for j in range(newlast_idx,n):
            if i==n_list[j]:
                count+=1
                last_idx = j
        for j in range(0,newlast_idx):
            if i==n_list[j]:
                count+=1
                last_idx = j

    if last_idx<=m:
        for k in range(last_idx,m+1):
            if n_list[k]==n_list[m]:
                count+=1

    else:
        for h in range(last_idx,n):
            if n_list[h]==n_list[m]:
                count+=1
        for l in range(0,m+1):
            if n_list[l]==n_list[m]:
                count+=1

    print(count)