import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

arr  = [0] + arr
if N < 3:
    print(sum(arr))
else:
    dp = [0]*(N+1)

    dp[1] = arr[1]
    dp[2] = arr[2]+arr[1]

    for i in range(3, N+1):
        dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i], dp[i-1])
    
    print(max(dp))