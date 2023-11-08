import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
a = 0
b = 0
c = 0
if T//300 >0:
    a = T//300
    T %= 300
if T//60>0:
    b = T//60
    T %= 60
if 1:
    c = T//10
    T %= 10
if T == 0:
    print(a, b, c)
else:
    print(-1)