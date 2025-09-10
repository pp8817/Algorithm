# DP 문제

def solution(land):
    N = len(land)
    dp = [[0]*4 for _ in range(N)]
    
    # 첫번째 땅 값 초기화
    for c in range(4):
        dp[0][c] = land[0][c]
    
    # 각 행에 대해, 바로 위 행의 최대값/차최대값만 이용
    for r in range(1, N):
        best = -1
        second = -1
        best_col = -1
        for c in range(4):
            val = dp[r-1][c]
            if val > best:
                second = best
                best = val
                best_col = c
            elif val > second:
                second = val

        # 이번 행 갱신: 같은 열이면 second, 아니면 best를 더함
        for c in range(4):
            add = best if c != best_col else second
            dp[r][c] = land[r][c] + add

    return max(dp[N-1])