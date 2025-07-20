import sys
input = lambda: sys.stdin.readline().rstrip()

T, W = map(int, input().split())
plums = [int(input()) for _ in range(T)]

# dp[t][w] = t초까지 w번 이동했을 때 받을 수 있는 자두 개수
dp = [[0]*(W+1) for _ in range(T+1)]

for t in range(1, T+1):
    for w in range(W+1):
        # 현재 자두가 떨어지는 나무
        curr_tree = plums[t-1]

        # 현재 위치
        curr_pos = 1 if w%2==0 else 2

        # 현재 위치에서 자두를 받을 수 있는지
        gain = 1 if curr_pos==curr_tree else 0

        if w == 0:
            dp[t][w] = dp[t-1][w] + gain
        else:
            dp[t][w] = max(
                # 이동하지 않고 현재 위치 유지
                dp[t-1][w] + gain,
                # 이전 위치에서 이동해서 현재 위치로 이동
                dp[t-1][w-1] + (1 if curr_tree==(2 if curr_pos==1 else 1) else 0)
            )

print(max(dp[T]))