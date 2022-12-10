import sys

def binary_search(lst,find_num):
    i = 0
    j = len(lst)-1

    while i<=j:
        mid = (i+j)//2
        if lst[mid]==find_num:
            return 1
        elif lst[mid]<find_num:
            i = mid+1
        else:
            j = mid-1
    return 0

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_list = list(map(int,sys.stdin.readline().split()))

n_list.sort()

for i in m_list:
    print(binary_search(n_list,i))