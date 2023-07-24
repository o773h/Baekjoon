import sys

alpha ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

lst = []
for i in range(len(a)):
    lst.append(num[alpha.find(a[i])])
    lst.append(num[alpha.find(b[i])])

while len(lst) !=2:
    new_lst = []
    for i in range(1,len(lst)):
        new_lst.append((lst[i-1] + lst[i]) % 10)
    lst = new_lst

result = str(lst[0]) + str(lst[1])
print(result)