def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    for y in range(1, n+1):
        for x in range(1, m+1):
            if [x, y] in puddles:
                continue
            b1 = dp[y-1][x]
            b2 = dp[y][x-1]
            
            dp[y][x] += b1 + b2
    
    return dp[n][m] % 1000000007
    