import sys

def solve(sum,i):
    if i==n:
        return 1 if sum==s else 0
    ret = 0
    ret +=solve(sum+n_list[i],i+1) + solve(sum,i+1)

    return ret

n,s = map(int,sys.stdin.readline().split())
n_list = list(map(int,sys.stdin.readline().split()))

result = solve(0,0)
if s==0:
    result-=1

print(result)