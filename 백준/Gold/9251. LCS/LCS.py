import sys
input = lambda: sys.stdin.readline().rstrip()

s1 = list(input())
s2 = list(input())

a = len(s1)+1
b = len(s2)+1
LCS = [[0]*b for _ in range(a)]

for i in range(1, a):
    for j in range(1, b):
        if s1[i-1] == s2[j-1]:
            LCS[i][j] = LCS[i-1][j-1]+1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(max(map(max, LCS)))