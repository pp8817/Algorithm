import sys
input = sys.stdin.readline

N = int(input())
prices = []

for i in range(N):
    prices.append(int(input()))

prices = sorted(prices, reverse=True)
for i in range(2, N, 3):
    prices[i] = 0
print(sum(prices))