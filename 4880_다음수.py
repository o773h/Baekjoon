import sys

while True:
    a,b,c = map(int,sys.stdin.readline().split())

    if a==0 and b==0 and c==0:
        break

    if (b-a) == (c-b):
        print("AP",2*c-b)
    else:
        print("GP",c*c//b)