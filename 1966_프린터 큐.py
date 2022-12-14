import sys

num = int(sys.stdin.readline())

# counts=[]


for _ in range(num):
    n,m = map(int,sys.stdin.readline().split())
    n_list = list(map(int,sys.stdin.readline().split()))
    count = 0
    last_idx=n

    print(n_list[m])

    
    for i in range(9,n_list[m],-1):
        for j in range(n):
            if i==n_list[j]:
                count+=1
                last_idx = j
        
    if last_idx<m:
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
#     counts.append(count)

# print(counts)

# solution = []
# for _ in range(100):
#     solution.append(int(sys.stdin.readline()))


# for i in range(100):
#     if counts[i]!=solution[i]:
#         print(i,'번째가 틀림')