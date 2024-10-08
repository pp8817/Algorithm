import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

N = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(N)])
h = []

for s, e in arr:
    if h and h[0] <= s: 
        heapq.heappop(h)
    heapq.heappush(h, e)

print(len(h))