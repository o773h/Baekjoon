import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    n_list = list(map(int,sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    m_list = list(map(int,sys.stdin.readline().split()))

    n_list.sort()

    for i in m_list:
        start = 0
        end = n
        flag = True
        while start < end:
            mid = (start + end) //2
            if i == n_list[mid]:
                print(1)
                flag = False
                break
            elif i < n_list[mid]:
                end = mid
            else:
                start = mid+1
        if flag:
            print(0)