import sys

del_str = {'C','A','M','B','R','I','D','G','E'}
st = sys.stdin.readline().strip()
for s in st:
    if s in del_str:
        continue

    print(s,end='') 