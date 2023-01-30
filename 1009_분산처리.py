import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a,b = map(int,sys.stdin.readline().split())
    aa = a
    aa %= 10
    lst = [aa]
    for i in range(1,b):
        aa*=a
        aa%=10
        if aa in lst:
            step = i - lst.index(aa)
            aa = lst[(b-1)%step]
            break
        else:
            lst.append(aa)

    print(aa if aa!=0 else 10)