import sys
import bisect

n_list = [True for _  in range(123456*2)]
n_list[0] = False
n_list[1] = False
prime_numbers = []

for i in range(2,123456*2):
    if n_list[i]:
        prime_numbers.append(i)
        for j in range(i*2,123456*2,i):
            n_list[j]= False

while True:
    n = int(sys.stdin.readline())
    if n==0:
        break
    
    print(bisect.bisect_right(prime_numbers,2*n) - bisect.bisect_right(prime_numbers,n))