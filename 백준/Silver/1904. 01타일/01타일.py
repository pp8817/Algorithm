import sys
input = lambda: sys.stdin.readline().rstrip()

MOD = 15746

N = int(input())

dp = [0]*(N+2)
dp[0], dp[1] = 1, 1

for i in range(2, N+1):
    dp[i] = (dp[i-1] + dp[i-2])%MOD

print(dp[N])