import sys

numbers = [True for _ in range(100000)]
numbers[0]=False
numbers[1]=False
prime_number=[]

for i in range(2,100000):
    if numbers[i]:
        prime_number.append(i)
        for j in range(i*2,100000,i):
            numbers[j] = False

n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    
    for i in prime_number:
        if num==1:
            break
        count = 0
        while num%i == 0: 
            num = num//i
            count +=1
        if count>0:
            print(i,count)