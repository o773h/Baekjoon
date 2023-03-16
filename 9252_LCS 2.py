import sys

s_a = sys.stdin.readline().rstrip()
s_b = sys.stdin.readline().rstrip()

l_a = len(s_a)
l_b = len(s_b)

lcs = [[0 for _ in range(l_a+1)] for _ in range(l_b+1)]

for i in range(1,l_a+1):
    for j in range(1,l_b+1):
        if s_a[i-1] == s_b[j-1]:
            lcs[j][i] = lcs[j-1][i-1]+1
        else:
            lcs[j][i] = max(lcs[j-1][i], lcs[j][i-1])

result = []

i = l_a
j = l_b
while i>0 and j>0:
    if lcs[j][i]==lcs[j-1][i]:
        j-=1
    elif lcs[j][i]==lcs[j][i-1]:
        i-=1
    else:
        result.append(s_b[j-1])
        i-=1
        j-=1

print(lcs[-1][-1])
if result:
    print(*result[::-1],sep='')