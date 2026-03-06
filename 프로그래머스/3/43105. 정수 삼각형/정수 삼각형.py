def solution(triangle):
    N = len(triangle)
    dp = [[0]*i for i in range(1, N+1)]
    dp[0][0] = triangle[0][0]
    
    for r in range(1, N):
        for c in range(r+1):
            if c == 0:
                dp[r][c] = dp[r-1][0] + triangle[r][c]
            elif c == r:
                dp[r][c] = dp[r-1][-1] + triangle[r][c]
            else:
                dp[r][c] = max(dp[r-1][c-1], dp[r-1][c]) + triangle[r][c]
    
    return max(dp[-1])