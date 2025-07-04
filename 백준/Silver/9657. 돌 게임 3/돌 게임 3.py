import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dp = [0]*(N+1) # 0: SK, 1: CY
if N>=2:
    dp[2] = 1

if N >= 5:
    for i in range(5, N+1):
        if dp[i-1] or dp[i-3] or dp[i-4]:
            dp[i] = 0
        else:
            dp[i] = 1

if dp[N] == 1:
    print("CY")
else:
    print("SK")