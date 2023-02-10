import sys

while True:
    n = int(sys.stdin.readline())
    if n==-1:
        break

    sum = 0
    divisor = []
    for i in range(1,n):
        if n%i==0:
            divisor.append(i)
            sum+=i
    
    if sum==n:
        print(n,'=',end=' ')
        print(*divisor,sep=' + ')
    else:
        print(n,"is NOT perfect.")