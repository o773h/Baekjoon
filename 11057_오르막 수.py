import sys

n = int(sys.stdin.readline())

numbers = [1 for _ in range(10)]

for i in range(n-1):
    for j in range(1,10):
        numbers[j] = numbers[j-1] +numbers[j]

print(sum(numbers)%10007)