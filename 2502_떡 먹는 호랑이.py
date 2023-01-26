import sys
A = {
    1:1,
    2:0
}

B = {
    1:0,
    2:1
}

d,k = map(int,sys.stdin.readline().split())

for i in range(3,d+1):
    A[i]=A[i-1]+A[i-2]
    B[i]=B[i-1]+B[i-2]

for i in range(1,k):
    if (k-i*A[d])%B[d]==0:
        print(i)
        print((k-i*A[d])//B[d])
        break