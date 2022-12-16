import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    n_list=[]
    for _ in range(n):
        n_list.append(int(sys.stdin.readline())-1)
    
    i = 0
    count = 0
    visited=[]
    while True:
        if n==1 and n_list[0]==0:
            print(1)
            break

        if i==(n-1):
            print(count)
            break

        if i not in visited:
            visited.append(i)
            i = n_list[i]
            count +=1
        else:
            print(0)
            break