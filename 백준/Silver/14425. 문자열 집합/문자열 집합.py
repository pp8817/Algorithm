import sys
n, m = map(int, sys.stdin.readline().split())
s = set()
c = 0
for _ in range(n):
    s.add(sys.stdin.readline())
for _ in range(m):
    if sys.stdin.readline() in s:
        c+=1
print(c)