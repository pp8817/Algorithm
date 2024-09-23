import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = [(0,0)]
for _ in range(N):
    t,p =  map(int, input().split())
    arr.append((t,p))

dp = [0]*(N+1)

for i in range(1, N+1):
    t1,p1 = arr[i]
    dp[i] = max(dp[i], dp[i-1])
    fin_date = i+t1-1
    if fin_date <= N:
        dp[fin_date] = max(dp[fin_date], dp[i-1] + p1)

print(max(dp))