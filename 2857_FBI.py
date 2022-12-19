import sys

lst = []
for i in range(1,6):
    name = sys.stdin.readline()
    if 'FBI' in name:
        lst.append(i)


if lst==[]:
    print("HE GOT AWAY!")
else:
    print(*lst,sep=' ')