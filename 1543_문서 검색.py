import sys

st = sys.stdin.readline().rstrip()
f = sys.stdin.readline().rstrip()
l = len(f)

result = 0
r = -l
while True:
    r = st.find(f,r+l)
    result+=1
    if r==-1:
        result-=1
        break

print(result)