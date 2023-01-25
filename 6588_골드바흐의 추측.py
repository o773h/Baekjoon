import sys
import bisect

n_list = [True for _ in range(1000001)]
n_list[0] = False
n_list[1] = False

prime_numbers=[]

for i in range(3,1000001,2):
    if n_list[i]==True:
        prime_numbers.append(i)
        for j in range(i,1000001,i):
            n_list[j]=False

while True:
    n = int(sys.stdin.readline())
    if n==0:
        break

    for i in prime_numbers:
        if i>n:
            print("Goldbach's conjecture is wrong.")
            break
        else:
            if bisect.bisect_left(prime_numbers,n-i)!=bisect.bisect_right(prime_numbers,n-i):
                print(n,"=",i,"+",n-i)
                break