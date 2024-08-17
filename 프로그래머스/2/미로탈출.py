def solution(n): # n: 멀리뛰기에 사용될 칸의 수
    
    if n in [1,2]:
        return n
    
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    answer = dp[n]%1234567
    return answer
