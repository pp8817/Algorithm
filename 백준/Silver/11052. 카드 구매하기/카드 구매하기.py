import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
P = [0] + list(map(int, input().split()))
dp = [0]*(N+1)

dp[1] = P[1]

for i in range(2, N+1):
    for j in range(1, i):
        dp[i] = max(dp[i-j]+P[j], P[i], dp[i])
print(dp[N])