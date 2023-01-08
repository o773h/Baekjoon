import sys
from itertools import combinations

vowel=['a','e','i','o','u']

l,c = map(int,sys.stdin.readline().split())
c_list = list(sys.stdin.readline().split())
c_list.sort()


for alphabet in combinations(c_list,l):
    password=""
    count_vowel = 0
    count_consonant = 0
    for i in alphabet:
        password+=i
        if i in vowel:
            count_vowel+=1
        else:
            count_consonant+=1
    if count_vowel>=1 and count_consonant>=2:
        print(password)