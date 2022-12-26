import sys

n,m = map(int,sys.stdin.readline().split())
num_dict = {}
for i in range(1,n+1):
    num_dict[str(i)] = (sys.stdin.readline().strip())

name_dict = dict(map(reversed,num_dict.items()))

for _ in range(m):
    question = sys.stdin.readline().strip()
    if num_dict.get(question):
        print(num_dict[question])
    else:
        print(name_dict[question])