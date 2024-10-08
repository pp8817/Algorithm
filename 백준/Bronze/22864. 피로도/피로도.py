import sys
input = lambda: sys.stdin.readline().rstrip()

A, B, C, M = map(int, input().split()) 

ans = 0
tmp = 0
for i in range(24):
    if (tmp+A) <= M:
        ans += B
        tmp += A
    else:
        tmp = max(0, tmp-C)

print(ans)