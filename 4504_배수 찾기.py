import sys

n = int(sys.stdin.readline())

while True:
    num = int(sys.stdin.readline())
    if num==0:
        break

    if num%n==0:
        print(num," is a multiple of ",n,".",sep='')
    else:
        print(num," is NOT a multiple of ",n,".",sep='')