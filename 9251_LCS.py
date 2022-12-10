word1 = input()
word2 = input()
lcs=[0 for _ in range(len(word2))]

for i in range(len(word1)):
    for j in range(len(word2)):
        if word2[j]==word1[i]:
            if j!=0:
                lcs[j]=max(lcs[:j]) +1
            else:
                lcs[j]=lcs[0]+1

print(max(lcs))