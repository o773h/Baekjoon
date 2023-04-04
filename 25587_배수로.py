import sys
sys.setrecursionlimit(1000000)

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b,result):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        if state[b]<0:
            if state[a]+state[b]>=0:
                result-=country[b]
        else:
            if state[a]+state[b]<0:
                result+=country[b]
        
        if state[a]<0:
            if state[a]+state[b]>=0:
                result-=country[a]
        else:
           if state[a]+state[b]<0:
                result+=country[a]

        state[a] += state[b]
        country[a] += country[b]
        parent[b] = a

    elif a>b:
        if state[b]<0:
            if state[a]+state[b]>=0:
                result-=country[b]
        else:
            if state[a]+state[b]<0:
                result+=country[b]
        
        if state[a]<0:
            if state[a]+state[b]>=0:
                result-=country[a]
        else:
           if state[a]+state[b]<0:
                result+=country[a]

        state[b] += state[a]
        country[b] += country[a]
        parent[a] = b

    return result


n,m = map(int,sys.stdin.readline().split())
parent = [i for i in range(n+1)]
country = [1 for _ in range(n+1)]

state = [0]
state.extend(list(map(int,sys.stdin.readline().split())))

precipitation = [0]
precipitation.extend(list(map(int,sys.stdin.readline().split())))

result = 0
for i in range(1,n+1):
    state[i] = state[i] -precipitation[i]
    if state[i]<0:
        result+=1

for _ in range(m):
    q = sys.stdin.readline().split()
    if q[0] == '2':
        print(result)
    else:
        x = int(q[1])
        y = int(q[2])
        result = union_parent(parent,x,y,result)