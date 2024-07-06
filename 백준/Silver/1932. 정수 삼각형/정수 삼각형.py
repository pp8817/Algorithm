import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
triangle = []

for i in range(n):
    triangle.append(list(map(int, input().split())))

dp = [[0]*i for i in range(1,n+1)]
dp[0][0] = triangle[0][0]

for i in range(1,n):
    for j in range(i+1):
        # dp[i][j]: i번째 행의 j번째 열까지의 최대 합
        if j==0: # 왼쪽 가장자리
            dp[i][j] = dp[i-1][j] + triangle[i][j]    
        elif j==i: # 오른쪽 가장자리
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]    
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

print(max(dp[-1]))

