import sys

n,p,q,x,y = map(int,sys.stdin.readline().split())

n_dict = dict()

def find(num):
    if num not in n_dict:
        if num<=0:
            n_dict[num] = 1
        else:
            n_dict[num] = find((num//p)-x) + find((num//q)-y)
    
    return n_dict[num]
    
print(find(n))