import sys

n = int(sys.stdin.readline())
not_nums = ['0','1','2','3','5','6','8','9']

while True:
    flag = True
    for i in str(n):
        if i in not_nums:
            flag = False
            break 
    if flag:
        break  
    n-=1

print(n)