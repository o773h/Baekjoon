import sys


n_list = [True for _  in range(100000)]
n_list[0] = False
n_list[1] = False
prime_numbers = []

for i in range(2,100000):
    if n_list[i]:
        prime_numbers.append(i)
        for j in range(i*2,100000,i):
            n_list[j]= False

a,b = map(int,sys.stdin.readline().split())
result = 0

for i in range(a,b+1):
    count = 0
    num = i
    for j in prime_numbers:
        if num==1:
            break
        while num%j==0:
            num = num // j
            count+=1
    if count in prime_numbers:
        result +=1

print(result)