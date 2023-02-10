import sys

n_list = [True for _ in range(1000001)]
n_list[0] = False
n_list[1] = False

prime_numbers=dict()

for i in range(3,1000001,2):
    if n_list[i]==True:
        prime_numbers[i]=0
        for j in range(i,1000001,i):
            n_list[j]=False

while True:
    n = int(sys.stdin.readline())
    if n==0:
        break

    for i in prime_numbers.keys():
        if (n-i) in prime_numbers:
            print(n,"=",i,"+",n-i)
            break
        if i>n:
            print(i,n)
            print("Goldbach's conjecture is wrong.")