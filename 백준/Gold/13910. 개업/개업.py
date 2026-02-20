import sys
input = lambda: sys.stdin.readline().rstrip()

INF = 10**9

N, M = map(int, input().split())
arr = list(map(int, input().split()))

cookables = set()

# 1개 웍
for a in arr:
    if a <= N:
        cookables.add(a)

# 2개 웍
for i in range(M):
    ai = arr[i]
    for j in range(i + 1, M):
        s = ai + arr[j]
        if s <= N:
            cookables.add(s)

if not cookables:
    print(-1)
    sys.exit(0)

cookables = sorted(cookables)

dp = [INF] * (N + 1)
dp[0] = 0

for x in range(1, N + 1):
    for c in cookables:
        if c > x:
            break
        dp[x] = min(dp[x], dp[x - c] + 1)

print(-1 if dp[N] == INF else dp[N])