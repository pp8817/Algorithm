import sys
input = sys.stdin.readline
N, L = map(int, input().split())

pools= sorted(tuple(map(int, input().split())) for i in range(N))

res, s = 0, 0
for start, end in pools:
    s = max(start, s)
    diff = end - s
    count = (diff + L - 1) // L
    res += count
    s += count * L

print(res)