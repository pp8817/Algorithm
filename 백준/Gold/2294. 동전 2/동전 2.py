import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
dp = [int(1e9)]*(100001) # i원을 만들 때 사용되는 동전의 갯수
coin = []
for _ in range(n):
    c = int(input())
    coin.append(c)
    dp[c] = 1

s = min(coin)

for i in range(s, k+1):
    if dp[i] == 0:
        continue

    for c in coin:
        if (i+c)<=k:
            dp[i+c] = min(dp[i]+1, dp[i+c])

if dp[k] == int(1e9):
    print(-1)
else:
    print(dp[k])