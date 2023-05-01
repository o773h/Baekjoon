import sys

n = int(sys.stdin.readline())
student = []
for _ in range(n):
    student.append(list(sys.stdin.readline().split()))

student.sort(key=lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for s in student:
    print(s[0])