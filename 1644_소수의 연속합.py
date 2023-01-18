import sys

n = int(sys.stdin.readline())

numbers = [True for _ in range(n+1)]
numbers[0] = False
numbers[1] = False

prime_numbers =[]
for i in range(2,n+1):
    if numbers[i]==True:
        prime_numbers.append(i)
        for j in range(i*2,n+1,i):
            numbers[j]=False

start = 0
end = 0
sum = 0
count = 0

while start<len(prime_numbers):
    if sum==n:
        count+=1

    if sum<n:
        if end==len(prime_numbers):
            break
        sum+=prime_numbers[end]
        end+=1
    else:
        sum-=prime_numbers[start]
        start+=1

print(count)
