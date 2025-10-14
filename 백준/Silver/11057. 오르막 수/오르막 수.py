import sys
input = lambda: sys.stdin.readline()

N = int(input())
MOD = 10007

dp = [[0]*10 for _ in range(N+1)] # i자리 수 중 끝자리가 j인 오르막 수의 개수

for j in range(10):
    dp[1][j] = 1

for i in range(2, N+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][k] for k in range(j+1)) % MOD

print(sum(dp[N]) % MOD)