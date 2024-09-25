import sys
input = lambda: sys.stdin.readline().rstrip()

C, N = map(int, input().split()) # target, 도시 개수
cities = [list(map(int, input().split())) for _ in range(N)] # 비용, 고객 수

INF = int(1e9)
dp = [INF]*(C+101)
dp[0] = 0

for cost, cus in cities:
    for i in range(cus, C+101):
        dp[i] = min(dp[i], dp[i-cus]+cost)

print(min(dp[C:]))