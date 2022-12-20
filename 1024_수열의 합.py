import sys

n,l = map(int,sys.stdin.readline().split())
flag = False

while True:
    if flag:
        break
    n_list = [i for i in range(n//l-l+1,n//l+1)]
    
    if n_list[0]<0:
        num = n_list[0]
        for j in range(l):
            n_list[j]-=num

    while True:
        if sum(n_list)==n:
            flag = True
            break
        elif sum(n_list)>n:
            l+=1
            break
        for j in range(l):
            n_list[j]+=1

    if l>100:
        flag=False
        break

if flag:
    print(*n_list)
else:
    print(-1)