import sys

s,k,h = map(int,sys.stdin.readline().split())

sum = s+k+h

if sum>=100:
    print('OK')
elif min(s,k,h)==s:
    print('Soongsil')
elif min(s,k,h)==k:
    print('Korea')
else:
    print('Hanyang')