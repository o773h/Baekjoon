import sys

n = int(sys.stdin.readline())
n_list = [i for i in range(1,n+1)]
flag = True

while len(n_list)!=1:
    length = len(n_list)
    new_list = []

    if flag:
        for i in range(1,length,2):
            new_list.append(n_list[i])
    else:
        for i in range(0,length,2):
            new_list.append(n_list[i])

    if new_list[-1]==n_list[-1]:
        flag = True
    else:
        flag = False

    n_list = new_list

print(n_list[0])