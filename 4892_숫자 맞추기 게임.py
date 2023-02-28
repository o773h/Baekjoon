import sys

i = 0
while True:
    n = int(sys.stdin.readline())
    if n==0:
        break
    i+=1

    result=str(i)+'. '
    n1 = 3*n
    if n1%2==0:
        result+='even '
        n2 = n1//2
    else:
        result+='odd '
        n2 = (n1+1)//2
    
    n3 = 3*n2
    n4 = n3//9
    result+=str(n4)

    print(result)