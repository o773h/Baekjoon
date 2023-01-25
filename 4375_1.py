import sys

for line in sys.stdin:
    n = int(line)
    num = '1'
    while True:
        if int(num)%n==0:
            print(len(num))
            break
        else:
            num+='1'