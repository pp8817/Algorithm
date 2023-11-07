import sys
input = lambda: sys.stdin.readline().rstrip()
def isPalindrome(n):
    global count
    count+=1
    if (len(n) == 0) or (len(n) == 1):
        return True
    else:
        return (n[0] == n[-1]) and (isPalindrome(n[1:-1]))

T = int(input())
for _ in range(T):
    str = input()
    count = 0
    if isPalindrome(str) == True:
        c = 1
    else:
        c=0
    print(c, count)