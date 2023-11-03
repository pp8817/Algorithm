import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
s = 1
b = 1
for i in range(1, K+1):
    s*=N
    N-=1
    
b = 1
if K>0:
    for j in range(1, K+1):
        b*=j
else:
    b=1

print(int(s/b))