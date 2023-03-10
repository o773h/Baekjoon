import sys

n = int(sys.stdin.readline())

adrian = 'ABC'*34
bruno = 'BABC'*25
goran = 'CCAABB'*17

a = 0
b = 0
g = 0

s = sys.stdin.readline().rstrip()

for i in range(n):
    if s[i]==adrian[i]:
        a+=1
    if s[i]==bruno[i]:
        b+=1
    if s[i]==goran[i]:
        g+=1

result = max(a,b,g)
print(result)
if result==a:
    print("Adrian")
if result==b:
    print("Bruno")
if result==g:
    print("Goran")