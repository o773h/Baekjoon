import sys

while True:
    s = sys.stdin.readline().strip()
    if s=='*':
        break
    flag = True
    for k in range(1,len(s)+1):
        d = dict()
        for i in range(0,len(s)-k):
            if s[i:i+k+1:k] not in d:
                d[s[i:i+k+1:k]] = True
            else:
                flag = False
                break
    if flag:
        print(s,"is surprising.")
    else:
        print(s,"is NOT surprising.")