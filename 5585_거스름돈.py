import sys

n = int(sys.stdin.readline())

result = 0
change = 1000-n

result += change//500
change%=500

result += change//100
change%=100

result += change//50
change%=50

result += change//10
change%=10

result += change//5
change%=5

result += change//1

print(result)