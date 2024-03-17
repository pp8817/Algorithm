import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if not len(arr):
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, x)