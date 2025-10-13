import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))

dp = [1]*N # LIS 길이 저장
prev = [-1]*N # 수열 추적용


for i in range(N):
    for j in range(i):
        if arr[j] < arr[i] and (dp[j]+1) > dp[i]:
            dp[i] = dp[j] + 1
            prev[i] = j

max_len = max(dp)
last_index = dp.index(max_len)

answer = []
while last_index != -1:
    answer.append(arr[last_index])
    last_index = prev[last_index]

answer.reverse()

print(max_len)
print(*answer)