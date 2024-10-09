import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

minus = []

for i in range(N-1):
    minus.append(arr[i]-arr[i+1])

if K == 1:
    print(sum(minus))
else:
    K -= 1
    minus.sort()
    print(sum(minus[:-K]))