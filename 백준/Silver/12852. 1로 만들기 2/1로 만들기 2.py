import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

dp = [int(1e9)]*(N+1)
dp[N] = 0

# 각 숫자에서 어떤 숫자로 갔는지 저장
parent = [-1]*(N+1)

for i in range(N, 1, -1):
    if i%3==0 and dp[i//3] > dp[i]+1:
        dp[i//3] = dp[i] + 1
        parent[i//3] = i
    if i%2==0 and dp[i//2] > dp[i]+1:
        dp[i//2] = dp[i] + 1
        parent[i//2] = i
    if dp[i-1] > dp[i]+1:
        dp[i-1] = dp[i]+1
        parent[i-1] = i

print(dp[1])
path = []
current = 1
while current != -1:
    path.append(current)
    current = parent[current]
path.reverse()
print(*path)