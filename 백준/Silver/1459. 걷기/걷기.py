import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

X, Y, W, S = map(int, input().split())

m1 = (X+Y)*W

if (X+Y)%2==0:
    m2 = max(X,Y)*S

else:
    m2 = (max(X,Y)-1)*S+W

m3 = (min(X,Y)*S) + (abs(X-Y)*W)

print(min(m1,m2,m3))