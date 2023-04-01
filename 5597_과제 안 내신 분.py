import sys

student = set()
for _ in range(28):
    student.add(int(sys.stdin.readline()))

for i in range(1,31):
    if i not in student:
        print(i)