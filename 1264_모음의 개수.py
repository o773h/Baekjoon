import sys

lst = ['a','e','i','o','u','A','E','I','O','U']
while True:
    count = 0
    str = sys.stdin.readline().strip()
    if str=='#':
        break

    for i in str:
        if i in lst:

            count+=1
    print(count)