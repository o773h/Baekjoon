import sys

while True:
    st = sys.stdin.readline().rstrip()
    
    if st=='END':
        break

    print(st[::-1])