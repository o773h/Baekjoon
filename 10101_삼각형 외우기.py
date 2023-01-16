import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if (a+b+c)!=180:
    print("Error")
else:
    if a==b:
        if b==c:
            print("Equilateral")
        else:
            print("Isosceles")
    elif a==c or b==c:
        print("Isosceles")
    else:
        print("Scalene")