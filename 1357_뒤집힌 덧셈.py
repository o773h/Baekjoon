import sys

def rev(num):
    str_num = str(num)
    str_num = str_num[::-1]
    return int(str_num)

x,y = map(int,sys.stdin.readline().split())

print(rev(rev(x)+rev(y)))