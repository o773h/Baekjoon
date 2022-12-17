import sys

n = int(sys.stdin.readline())

n_list = [True for _ in range(1004000+1)]

n_list[0] = False
n_list[1] = False

for i in range(2,len(n_list)):
    if n_list[i]==True:
        for j in range(i*2,len(n_list),i):
                n_list[j]=False


for i in range(n,len(n_list)):
    if n_list[i]==True:
        num = str(i)
        if num==num[::-1]:
            print(num)
            break           