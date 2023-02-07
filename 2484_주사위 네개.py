import sys

n = int(sys.stdin.readline())
result = []
for _ in range(n):
    a,b,c,d = map(int,sys.stdin.readline().split())
    if a==b==c==d:
        result.append(50000 + a*5000)
    elif a==b:
        if a==c:
            result.append(10000 + a*1000)
        elif a==d:
            result.append(10000 + a*1000)
        else:
            if c==d:
                result.append(2000+a*500+c*500)
            else:
                result.append(1000 + a*100)
    elif a==c:
        if a==d:
            result.append(10000 + a*1000)
        else:
            if b==d:
                result.append(2000+a*500+b*500)
            else:
                result.append(1000 + a*100)
    elif a==d:
        if b==c:
            result.append(2000+a*500+b*500)
        else:
            result.append(1000 + a*100)
    elif b==c:
        if b==d:
            result.append(10000 + b*1000)
        else:
            result.append(1000 + b*100)
    elif b==d:
        result.append(1000 + b*100)
    elif c==d:
        result.append(1000 + c*100)
    else:
        result.append(max(a,b,c,d)*100)

print(max(result))