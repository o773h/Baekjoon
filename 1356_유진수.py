import sys

n = sys.stdin.readline().rstrip()

result = 'NO'
if n!='1':
    for i in range(len(n)):
        mul1 = 1
        mul2 = 1
        for j in n[:i]:
            mul1 *= int(j)
        for j in n[i:]:
            mul2 *= int(j)
        
        if mul1 == mul2:
            result = 'YES'
            break
        

print(result)