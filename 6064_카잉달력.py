import sys

t = int(sys.stdin.readline())
for _ in range(t):
    m,n,x,y = map(int,sys.stdin.readline().split())

    if m<n:
        result = y
        if y>m:
            s = y%m
            if s==0:
                s = m
        else:
            s = y

        while s!=x:
            s+=n%m
            if s>m:
                s = s%m
            result+=n

            if result>m*n:
                result=-1
                break

    elif m>n:
        result = x
        if x>n:
            s = x%n
            if s==0:
                s = n
        else:
            s = x

        while s!=y:
            s+=m%n
            if s>n:
                s = s%n
            result+=m

            if result>m*n:
                result=-1
                break
    else:
        if x==y:
            result=x
        else:
            result=-1

    print(result)






# i = 1
# j = 1
# while True:
#     print("<",i,":",j,">")

#     if i==13 and j==11:
#         break

#     i+=1
#     j+=1
#     if i==14:
#         i = 1
#     if j==12:
#         j = 1
