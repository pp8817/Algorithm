import sys
input = lambda: sys.stdin.readline().rstrip()

index = 1
INF = float('inf')
while True:
    N = int(input())
    if N == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(N)]

    dp = [[INF]*3 for _ in range(N)]

    dp[0][0] = INF
    dp[0][1] = graph[0][1]
    dp[0][2] = graph[0][1] + graph[0][2]

    for i in range(1, N):
        dp[i][0] = graph[i][0] + min(dp[i-1][0], dp[i-1][1])
        dp[i][1] = graph[i][1] + min(dp[i][0], dp[i-1][0], dp[i-1][1], dp[i-1][2])
        dp[i][2] = graph[i][2] + min(dp[i][1], dp[i-1][1], dp[i-1][2])

    
    print(f"{index}. {dp[N-1][1]}")
    index += 1