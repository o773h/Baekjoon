import sys

n = int(sys.stdin.readline())

n_list = []
stk = []
for _ in range(n):
    n_list.append(int(sys.stdin.readline()))
count = 1
result = []
flag = True

for i in n_list:
    while True:
        if stk==[] or i>stk[-1]:
            result.append('+')
            stk.append(count)
            count+=1
        elif i==stk[-1]:
            result.append('-')
            del stk[-1]
            break
        else:
            flag=False
            break

if flag:
    print('\n'.join(result))
else:
    print('NO')
