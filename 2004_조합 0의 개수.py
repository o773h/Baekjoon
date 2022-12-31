import sys

n,m = map(int,sys.stdin.readline().split())

def div(n,num):
    count = 0
    while n>=num:
        count += n//num
        n = n//num
    return count

print(min(div(n,5)-div(m,5)-div((n-m),5),div(n,2)-div(m,2)-div((n-m),2)))