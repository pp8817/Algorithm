import sys
input = sys.stdin.readline

N = int(input()) #O(NlogN)
tips = []
for i in range(N):
    tips.append(int(input()))

tips = sorted(tips, reverse=True)

total = 0
for i, t in enumerate(tips):
    
    tip = t-i
    if tip >0:
        total+=tip
print(total)