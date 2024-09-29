import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))

# 경우는 2가지.
# 꿀통이 양 끝에 있는 경우
# 벌통이 중간에 있는 경우

prefix_sum = [0]*N
prefix_sum[0] = arr[0]

# 누적합
for i in range(1, N):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

# 벌통이 맨 왼쪽
case1 = 0
for i in range(1, N-1):
    case1 = max(case1, (prefix_sum[N-1]-arr[N-1]-arr[i]) + prefix_sum[i-1])

case2 = 0
for i in range(1, N-1):
    case2 = max(case2, (prefix_sum[N-1] - arr[0] - arr[i]) + (prefix_sum[N-1] - prefix_sum[i]))

case3 = 0
for i in range(1, N-1):
    case3 = max(case3, (prefix_sum[i]-arr[0]) + (prefix_sum[N-1]-prefix_sum[i-1]-arr[-1]))

print(max(case1, case2, case3))