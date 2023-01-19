import sys

def isPalindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False


t = int(sys.stdin.readline())

for _ in range(t):
    s = sys.stdin.readline().strip()
    
    start= 0
    end = len(s)-1
    result = 0
    while start<end:
        if s[start]!=s[end]:
            bool1 = isPalindrome(s[:start]+s[start+1:])
            bool2 = isPalindrome(s[:end]+s[end+1:])
            if bool1 or bool2:
                result = 1
                break
            else:
                result = 2
                break
        else:
            start +=1
            end -=1
    print(result)