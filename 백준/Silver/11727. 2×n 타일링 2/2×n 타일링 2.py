import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

DP = [0]*(1001)
DP[1] = 1
DP[2] = 3

# 점화식: f(x) = f(x-1) + 2*f(x-2)

for i in range(3, n+1):
    DP[i] = DP[i-1]+2*DP[i-2]
print(DP[n]%10007)