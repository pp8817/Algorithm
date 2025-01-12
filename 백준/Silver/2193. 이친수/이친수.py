import sys
input = lambda: sys.stdin.readline().rstrip()

# 이친수 구하기
# 1. 이친수는 0으로 시작하지 않는다 -> 반드시 1로 시작
# 2. 1이 두 번 연속으로 나타나지 않는다. -> 0은 상관 없음
# ex) 1, 10, 100, 101, 1000, 1001

# N자리 이친수 개수 구하기
# 1~N-1 자리 이친수의 개수를 구하고 N-1자리 이친수에 끝자리가 0 or 1이 붙는 경우를 추가하면 됨
N = int(input())
dp = [0]*(N+1)
dp[1] = 1
# 각 이친수의 끝자리가 0인 수를 따로 측정 -> 0인 경우에는 끝자리에 0,1 추가 가능
# 1인 경우에는 끝자리에 0만 추가 가능
temp = [0]*(N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + temp[i-1]
    temp[i] = temp[i-1] + (dp[i-1] - temp[i-1])
print(dp[N])