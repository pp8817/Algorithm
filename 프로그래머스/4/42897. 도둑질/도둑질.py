def solution(money):
    def sol(arr):
        n = len(arr)
        if n == 1:
            return arr[0]
        if n == 2:
            return max(arr)
        
        dp = [0]*n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+arr[i])
        
        return dp[-1]
    
    return max(sol(money[:-1]), sol(money[1:]))