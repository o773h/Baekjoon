import sys

expression = sys.stdin.readline().strip()

lst = []
start = 0
for i in range(len(expression)):
    if expression[i]=='-' or expression[i]=='+':
        lst.append(int(expression[start:i]))
        lst.append(expression[i])
        start = i+1
    elif i==(len(expression)-1):
        lst.append(int(expression[start:i+1]))

j = 0
while '+' in lst:
    if lst[j]=='+':
        lst[j-1] = lst[j-1]+lst[j+1]
        del lst[j]
        del lst[j]
        j-=1
        
    j+=1

j = 0
while '-' in lst:
    if lst[j]=='-':
        lst[j-1] = lst[j-1]-lst[j+1]
        del lst[j]
        del lst[j]
        j-=1
        
    j+=1

print(lst[0])
