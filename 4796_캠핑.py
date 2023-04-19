import sys

i = 0
while True:
    i+=1
    l,p,v = map(int,sys.stdin.readline().split())

    if l==0:
        break

    result = l * (v//p)

    if v%p > l:
        result+=l
    else:
        result += v%p
    
    print("Case {}: {}".format(i,result))