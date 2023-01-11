import sys

n,p,q = map(int,sys.stdin.readline().split())

n_dict = {0:1}

def find(num):
    if num not in n_dict:
        n_dict[num] = find(num//p) + find(num//q)
    
    return n_dict[num]
    
print(find(n))