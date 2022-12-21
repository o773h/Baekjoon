import sys

n,l = map(int,sys.stdin.readline().split())
n_list = list(map(int,sys.stdin.readline().split()))

n_list.sort()
count = 0
left = 0
start = 0
for i in n_list:
    if left>=i-start:
        left-=i-start
        start = i
    else:
        count+=1
        left = l
        left -=1
        start = i

print(count)