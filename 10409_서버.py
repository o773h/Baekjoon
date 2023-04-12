import sys

n,t = map(int,sys.stdin.readline().split())
n_list = list(map(int,sys.stdin.readline().split()))

count = 0
for num in n_list:
    if t>=num:
        t-=num
        count+=1
    else:
        break

print(count)