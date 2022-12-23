import sys

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int,sys.stdin.readline().split()))

n_list.sort()

for i in range(m):
    start = 0
    end = n
    flag = True
    
    while start<end:
        mid = (start+end)//2
        if m_list[i]==n_list[mid]:
            m_list[i]=1
            flag = False
            break            
        elif m_list[i]<n_list[mid]:
            end = mid
        else:
            start = mid+1
        
    if flag:
        m_list[i]=0

print(*m_list)