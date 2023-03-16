import sys
sys.setrecursionlimit(int(1e6))

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]


g = int(sys.stdin.readline())
p = int(sys.stdin.readline())

parent = [i for i in range(g+1)]
planes = []
for _ in range(p):
    planes.append(int(sys.stdin.readline()))

result = 0
for plane in planes:
    p = find_parent(parent,plane)
    if p==0:
        break
    parent[p]-=1
    result+=1

print(result)   