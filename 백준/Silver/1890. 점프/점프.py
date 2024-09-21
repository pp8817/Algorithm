import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input()) 
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)] # 각 위치까지 도달하는 점의 수
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        r,c = i,j
        if dp[r][c] == 0:
            continue
        move = board[r][c]
        if move == 0:
            continue
        r_move, c_move = r+move, c+move
        if r+move<N:
            if dp[r_move][c] == 0:
                dp[r_move][c] = dp[r][c]
            else:
                dp[r_move][c] += dp[r][c]
        if c+move<N:
            if dp[r][c_move] == 0:
                dp[r][c_move] = dp[r][c]
            else:
                dp[r][c_move] += dp[r][c]

print(dp[N-1][N-1])