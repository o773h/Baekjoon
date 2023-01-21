import sys

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))
n_list.sort()

sum = abs(n_list[0]+n_list[1]+n_list[2])
n1,n2,n3 = n_list[0],n_list[1],n_list[2]

for i in range(n-2):
    end = n-1

    for j in range(i+1,n-1):
        if j>=end:
            break

        while j<end-1 and abs(n_list[i]+n_list[j]+n_list[end-1])<abs(n_list[i]+n_list[j]+n_list[end]):
            end-=1

        if sum > abs(n_list[i]+n_list[j]+n_list[end]):
            sum = abs(n_list[i]+n_list[j]+n_list[end])
            n1,n2,n3 = n_list[i],n_list[j],n_list[end]
            
            if sum == 0:
                break


print(n1,n2,n3)