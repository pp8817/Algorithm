import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort()

dp = [0]*(k+1) # i원을 만들 때 사용되는 동전의 갯수
dp[0] = 1
for c in coins:
    for i in range(c, k+1):
        dp[i] += dp[i-c]

print(dp[k])