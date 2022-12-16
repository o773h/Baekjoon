import sys
import copy

def max_list(n_list):
    lst = copy.deepcopy(n_list)
    if len(lst)==1:
        print(max(lst[0]),end=' ')
    else:
        for i in range(1,len(lst)):
            lst[i][0] = max(lst[i-1][0]+lst[i][0],lst[i-1][1]+lst[i][0])
            lst[i][1] = max(lst[i-1][0]+lst[i][1],lst[i-1][1]+lst[i][1],lst[i-1][2]+lst[i][1])
            lst[i][2] = max(lst[i-1][1]+lst[i][2],lst[i-1][2]+lst[i][2])
        
        print(max(lst[-1]),end=' ')

def min_list(lst):
    if len(lst)==1:
        print(min(lst[0]))
    else:
        for i in range(1,len(lst)):
            lst[i][0] = min(lst[i-1][0]+lst[i][0],lst[i-1][1]+lst[i][0])
            lst[i][1] = min(lst[i-1][0]+lst[i][1],lst[i-1][1]+lst[i][1],lst[i-1][2]+lst[i][1])
            lst[i][2] = min(lst[i-1][1]+lst[i][2],lst[i-1][2]+lst[i][2])
        
        print(min(lst[-1]))

n = int(sys.stdin.readline())
n_list =[]
for _ in range(n):
    n_list.append(list(map(int,sys.stdin.readline().split())))

max_list(n_list)
min_list(n_list)