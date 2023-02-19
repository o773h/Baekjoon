import sys

n = int(sys.stdin.readline())
rope = []
for _ in range(n):
    rope.append(int(sys.stdin.readline()))

rope.sort(reverse=True)
result = [0 for _ in range(n)]

for i in range(n):
    result[i] = rope[i] * (i+1)

print(max(result))