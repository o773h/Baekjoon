import sys

m,n = map(int,sys.stdin.readline().split())

n_list = [True for i in range(n+1)]

n_list[0] = False
n_list[1] = False

for i in range(2,n+1):
    if n_list[i]==True:
        for j in range(i*2,n+1,i):
                n_list[j]=False


for i in range(m,n+1):
    if n_list[i]==True:
        print(i)