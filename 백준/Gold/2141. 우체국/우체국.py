import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = []
total_p = 0
for _ in range(N):
    x, a = map(int, input().split())
    arr.append([x,a])
    total_p += a

arr = sorted(arr, key = lambda x: x[0])

c = 0
for x, a in arr:
    c += a
    if c >= total_p/2:
        print(x)
        break