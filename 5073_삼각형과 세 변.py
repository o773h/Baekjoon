import sys

while True:
    a = list(map(int,sys.stdin.readline().split()))
    if a[0]==a[1]==a[2]==0:
        break
    a.sort()
    if a[0]+a[1]<=a[2]:
        print("Invalid")
    else:
        if a[0]==a[1]==a[2]:
            print("Equilateral")
        elif a[0]==a[1]:
            print("Isosceles")
        elif a[0]==a[2]:
            print("Isosceles")
        elif a[1]==a[2]:
            print("Isosceles")
        else:
            print("Scalene")