import sys
input = lambda: sys.stdin.readline().rstrip()

# 1 ≤ N ≤ 100,000
# 1 ≤ M ≤ 100,000
# 1 ≤ i ≤ j ≤ N

N, M = map(int, input().split())
arr = list(map(int, input().split())) #1000보다 작거나 같은 자연수들
sum_arr = [0]
total = 0
for i in arr:
    total += i
    sum_arr.append(total)
# 합을 구해야 하는 i와 j
for _ in range(M):
    i, j = map(int, input().split())
    print(sum_arr[j]-sum_arr[i-1])