import sys

s_a = sys.stdin.readline().rstrip()
s_b = sys.stdin.readline().rstrip()

l_a = len(s_a)
l_b = len(s_b)

lcs = [[0 for _ in range(l_b+1)] for _ in range(l_a+1)]

for i in range(1,l_a+1):
    for j in range(1,l_b+1):
        if s_a[i-1] == s_b[j-1]:
            lcs[i][j] = lcs[i-1][j-1]+1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[-1][-1])