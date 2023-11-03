import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
s = 1
b = 1
for i in range(1, K+1):
    s*=N
    N-=1
    
b = 1
for j in range(2, K+1):
        b*=j

print(int(s/b))