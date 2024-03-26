import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

N = int(input())

arr = []
for _ in range(N):
    x = int(input())

    if x > 0:
        heapq.heappush(arr, -x)
    elif x==0:
        if len(arr)==0:
            print(0)
        else:
            print(-heapq.heappop(arr))
