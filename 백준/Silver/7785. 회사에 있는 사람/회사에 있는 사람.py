import sys
n = int(sys.stdin.readline())
s = set()
for i in range(n):
    a, b = sys.stdin.readline().split()
    if a in s:
        s.remove(a)
    else:
        s.add(a)
s = sorted(s, reverse=True)
for i in s:
    print(i)