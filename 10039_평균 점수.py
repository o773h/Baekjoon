import sys

sum = 0
for _ in range(5):
    num = int(sys.stdin.readline())
    if num<40:
        sum+=40
    else:
        sum+=num

print(sum//5)