import sys

p = int(sys.stdin.readline())
n_list = []
result = []
for _ in range(p):
    n_list = list(map(int,sys.stdin.readline().split()))
    i = 1
    count = 0
    for i in range(1,21):
        for j in range(1,i):
            if n_list[i]<n_list[j]:
                n_list.insert(j,n_list.pop(i))
                count+=i-j

    print(n_list[0],count)