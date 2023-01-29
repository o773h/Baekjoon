import sys

while True:
    x = sys.stdin.readline()

    if x=='':
        break

    x = 10000000* int(x)
    n = int(sys.stdin.readline())
    n_list = []
    for _ in range(n):
        n_list.append(int(sys.stdin.readline()))

    n_list.sort()
    flag = True
    start = 0
    end = n-1

    while start<end:
        sum = n_list[start] + n_list[end]
        if sum==x:
            print("yes",n_list[start],n_list[end])
            flag = False
            break
        elif sum>x:
            end-=1
        else:
            start+=1
    
    if flag:
        print("danger")