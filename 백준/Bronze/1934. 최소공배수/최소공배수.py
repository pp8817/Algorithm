import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    aa, bb = a, b
    while bb != 0:
        aa = aa%bb
        aa, bb = bb, aa
        
    print(a*b//aa)