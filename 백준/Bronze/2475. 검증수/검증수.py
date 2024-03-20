import sys
input = lambda: sys.stdin.readline().rstrip()

li = list(map(int, input().split()))
s = 0
for i in li:
    s += (i**2)
print(s%10)