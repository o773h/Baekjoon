import sys

grades = {"A+": 4.3, "A0": 4.0, "A-": 3.7,
"B+": 3.3, "B0": 3.0, "B-": 2.7,
"C+": 2.3, "C0": 2.0, "C-": 1.7,
"D+": 1.3, "D0": 1.0, "D-": 0.7,
"F": 0.0}

n = int(sys.stdin.readline())
result = 0
count = 0
for _ in range(n):
    subject, credit, grade = sys.stdin.readline().split()
    result+= int(credit) * int(grades[grade] * 10)
    count += int(credit)

result = result*100//count


if result%10>=5:
    result = result//10 +1
else:
    result = result//10

print("%.2f"%(result/100))