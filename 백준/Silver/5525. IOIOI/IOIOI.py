import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
S = input()

Pn = ""
if N == 1:
    Pn = "IOI"
else:
    Pn = "IOI" + "OI"*(N-1)

pl = len(Pn)
c = 0
for i in range(M-pl+1):
    if S[i]=='I':
        if S[i:i+pl] == Pn:
            c+=1
print(c)