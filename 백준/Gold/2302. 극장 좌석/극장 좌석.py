import sys
input = lambda: sys.stdin.readline()

N = int(input())
M = int(input())
vips = [int(input()) for _ in range(M)]

fib = [0]*(N+1)
fib[0] = fib[1] = 1
for i in range(2, N+1):
    fib[i] = fib[i-1] + fib[i-2]

answer = 1
prev = 0

for vip in vips:
    gap = vip-prev-1
    answer *= fib[gap]
    prev = vip

answer *= fib[N - prev]

print(answer)