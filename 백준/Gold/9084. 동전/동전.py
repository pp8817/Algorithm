import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

# 2차원 테이블 코드
# for _ in range(T):
#     N = int(input()) # 동전의 가지 수
#     coins = list(map(int, input().split())) # 동전의 각 금액, 오름차순
#     coins.insert(0,0)
#     M = int(input()) # 목표 금액

#     dp = [[0]*(M+1) for _ in range(N+1)] # 2차원 테이블, 각 코인으로 금액을 만들 수 있는 경우의 수
#     for i in range(N+1):
#         dp[i][0] = 1

#     for i in range(1, N+1):
#         for j in range(1, M+1):
#             dp[i][j] = dp[i-1][j]
#             if j - coins[i] >= 0:
#                 dp[i][j] += dp[i][j-coins[i]]
#     print(dp[N][M])

# 1차원 테이블 코드
for _ in range(T):
    N = int(input()) # 동전의 가지 수
    coins = list(map(int, input().split())) # 동전의 각 금액, 오름차순
    M = int(input())

    dp = [0]*(M+1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, M+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[M])