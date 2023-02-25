import sys

alpha = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

s = sys.stdin.readline().strip()
result = 0
for i in range(1,len(s)+1):
    if s[-i] in alpha:
        result += alpha[s[-i]] * (16 ** (i-1))
    else:
        result += int(s[-i]) * (16 ** (i-1))

print(result)