import sys

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b


case = 0
while True:
    case+=1
    n,m = map(int,sys.stdin.readline().split())
    parent = [i for i in range(n+1)]
    if n == 0 and m == 0:
        break
    
    for _ in range(m):
        a,b = map(int,sys.stdin.readline().split())

        if find_parent(parent,a)!=find_parent(parent,b):
            union_parent(parent,a,b)
        else:
            union_parent(parent,a,0)
        
    root = set()
    for i in range(n+1):
        root.add(find_parent(parent,i))

    result = len(root)-1
    
    if result==0:
        print("Case ",case,": No trees.",sep='')
    elif result==1:
        print("Case ",case,": There is one tree.",sep='')
    else:
        print("Case ",case,": A forest of ",result," trees.",sep='')