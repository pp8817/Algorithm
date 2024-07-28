import sys
input = lambda: sys.stdin.readline().rstrip()

def Dynamic(weights, values, k):
    n = len(weights)
    dp = [[0]*(k+1) for _ in range(n+1)] # dp[i][w]: 첫번째 물품부터 i번째 물품까지 고려하고, 배낭의 용량이 w일때 최대 가치

    for i in range(1, n+1):
        for w in range(1, k+1):
            if weights[i-1]<=w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]]+values[i-1])
            else: 
                dp[i][w] = dp[i-1][w]
    return dp[n][k]


N, K = map(int, input().split()) # 물품의 수, 버틸 수 있는 무게

w = []
v = []
for _ in range(N):
    W,V = map(int, input().split()) # 물품 무게, 물품 가치
    w.append(W)
    v.append(V)
print(Dynamic(w,v,K))