import sys

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))

sum = 0
square_sum = 0

for i in n_list:
    sum+=i
    square_sum+=i**2

print((sum**2 - square_sum)//2)