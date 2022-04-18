n = int(input())

result = 0
if n%5==0:
    result = n//5
else:
    while True:
        if n==0:
            break
        elif n<3:
            result=-1
            break
        n-=3
        result+=1
        if n%5==0:
            result+= n//5
            break

print(result)