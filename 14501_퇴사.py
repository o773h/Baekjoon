n = int(input())
t_p = []

for i in range(n):
    t_p.append(list(map(int,input().split())))

t_p.append([0,0])

max_p = [0] * (n+1)

for i in range(n+1):
    for j in range(i):
        if t_p[j][0]== i-j:
            max_p[i] = max(max_p[i],max_p[i - t_p[j][0]] + t_p[j][1])
    max_p[i] = max(max_p[i],max_p[i-1])

print(max_p[-1])
