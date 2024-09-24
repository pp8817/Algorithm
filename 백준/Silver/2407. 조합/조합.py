import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

dp = [0]*(n+1)
dp[1], dp[2], dp[3] = 1, 2, 6

for i in range(4, n+1):
    dp[i] = i*dp[i-1]

print(dp[n]//(dp[m]*dp[n-m]))