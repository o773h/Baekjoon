import sys

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))

y_cost = 0
m_cost = 0

for i in n_list:
    y_cost +=((i//30)+1)*10
    m_cost +=((i//60)+1)*15

if y_cost<m_cost:
    print('Y',y_cost)
elif y_cost>m_cost:
    print('M',m_cost)
else:
    print('Y M',y_cost)