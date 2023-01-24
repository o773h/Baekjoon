import sys

def find(n,r,c):
    area = 2**(n-1) * 2**(n-1)
    if n==-1:
        return 0

    if r<2**(n-1):
        if c<2**(n-1):
            return find(n-1,r,c)
        else:
            return area + find(n-1,r,c%(2**(n-1)))
    
    else:
        if c<2**(n-1):
            return area*2 + find(n-1,r%(2**(n-1)),c)
        else:
            return area*3 + find(n-1,r%(2**(n-1)),c%(2**(n-1)))


n,r,c = map(int,sys.stdin.readline().split())
print(find(n,r,c))