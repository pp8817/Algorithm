import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coin = [0]*N
count = 0
for i in range(N):
    coin[i] = int(input())

coin.reverse()

for i in range(N):
    if K >= coin[i]:
        count += K//coin[i]
        K%=coin[i]
print(count)