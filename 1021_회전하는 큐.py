import sys

n,m = map(int,sys.stdin.readline().split())
n_list = [i for i in range(n,0,-1)]
find_list = list(map(int,sys.stdin.readline().split()))
count = 0
for i in find_list:
    idx = n_list.index(i)
    if n_list[-1]==i:
        n_list.pop()
    else:
        if (len(n_list)-1)-idx < idx+1:
            count += (len(n_list)-1)-idx
        else:
            count += idx+1
        n_list = n_list[idx+1:]+n_list[:idx+1]
        n_list.pop()

print(count)