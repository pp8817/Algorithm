import sys
input = lambda: sys.stdin.readline().rstrip()

S = int(input())

cou = 0
i = 0
c = 0
while S>=cou:
    i += 1
    cou += i
print(i-1)