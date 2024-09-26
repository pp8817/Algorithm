import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split()) #N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)
dp = [[0]*(K+1) for _ in range(N+1)]

dp[0][0] = 1
for i in range(N+1):
    for j in range(1, K+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000000

print(dp[N][K])