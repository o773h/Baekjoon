import sys

n = int(sys.stdin.readline())
numbers=[]

for i in range(n):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

for j in numbers:
    print(j)