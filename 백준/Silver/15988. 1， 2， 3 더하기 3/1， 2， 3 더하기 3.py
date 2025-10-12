import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
test = [int(input()) for _ in range(T)]

MAX = max(test) + 1
MOD = 1_000_000_009

dp = [0]*MAX
dp[0] = 1

for i in range(1, MAX):
    dp[i] = dp[i-1]
    if i>=2:
        dp[i] = (dp[i] + dp[i-2])%MOD
    if i>=3:
        dp[i] = (dp[i] + dp[i-3])%MOD

for t in test:
    print(dp[t])