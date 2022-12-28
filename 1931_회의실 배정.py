import sys

n = int(sys.stdin.readline())
n_list = []

for _ in range(n):
    n_list.append(list(map(int,sys.stdin.readline().split())))

n_list.sort()

end = n_list[0][1]
count = 1

for i in range(1,n):
    if n_list[i][0]>=end:
        count+=1
        end = n_list[i][1]
    elif n_list[i][1]<end:
        end = n_list[i][1]

print(count)