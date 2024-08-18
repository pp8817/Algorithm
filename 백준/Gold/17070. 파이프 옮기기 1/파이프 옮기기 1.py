import sys
input = lambda: sys.stdin.readline().rstrip()

def sol(): 
    dp[0][0][1]=1
    for i in range(2,N):
        if home[0][i] == 0:
            dp[0][0][i] = dp[0][0][i-1]

    # 대각선 파이프 처리
    for r in range(1, N):
        for c in range(1, N):
            if (home[r][c] + home[r][c-1] + home[r-1][c]) == 0:
                dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

            if home[r][c] == 0:
                dp[0][r][c] = dp[0][r][c-1] + dp[2][r][c-1]
                dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c]

    print(sum(dp[i][N-1][N-1] for i in range(3)))

N = int(input())
home = []
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

for _ in range(N):
    home.append(list(map(int, input().split())))

sol()