import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
P = list(map(int, input().split()))

P.sort(reverse=True)
s = 0
for i in range(N):
    s += P[i] * (i+1)
    
print(s)