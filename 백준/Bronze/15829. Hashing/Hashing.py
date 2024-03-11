import sys
input = lambda: sys.stdin.readline().rstrip()

L = int(input())
s = input()

answer = 0
for i in range(L):
    st = s[i]
    answer += (ord(st)-96)*(31**i)
print(answer)