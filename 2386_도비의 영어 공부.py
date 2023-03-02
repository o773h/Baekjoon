import sys

while True:
    alpha,*st = sys.stdin.readline().strip()
    
    if alpha=='#':
        break

    result = 0
    for s in st:
        if s==alpha or s==alpha.upper():
            result+=1
    
    print(alpha,result)