import sys
input = lambda: sys.stdin.readline().rstrip()
import math

N = int(input())
dp = [int(1e9)]*(N+1) # 1~N의 제곱수 항 최소 개수를 표현할 리스트
for i in range(1, int(math.sqrt(N))+1):
    dp[i**2] = 1

for i in range(2, N+1):
    if dp[i] == 1:
        continue
    
    for j in range(int(math.sqrt(i)), 0, -1):
        if dp[i] > 1+dp[i-j**2]:
            dp[i] = 1+dp[i-j**2]

print(dp[N])