import sys

n = int(sys.stdin.readline())
n_list = []

for _ in range(n):
    n_list.append(sys.stdin.readline().strip())

length = len(n_list[0])
k = 0

for i in range(1,length+1):
    new_list = []
    for j in range(n):
        if n_list[j][-i:] in new_list:
            break
        else:
            new_list.append(n_list[j][-i:])
    
    if len(new_list)==n:
        k = i
        break

print(k)