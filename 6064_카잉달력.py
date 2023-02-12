import sys

a = 1
b = 1
i = 1
while True:
    #print(i,"번째:""<",a,":",b,">")
    a+=1
    b+=1
    i+=1
    if a==40001:
        if b==40000:
            break
        a = 1
    
    if b==40001:
        b = 1
print(i)