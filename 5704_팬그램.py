import sys

while True:
    st = sys.stdin.readline().rstrip()
    if st=='*':
        break
    st_set = set()
    for s in st:
        if s==' ':
            continue
        st_set.add(s)
    if len(st_set) == 26:
        print('Y')
    else:
        print('N')