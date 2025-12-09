import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cnt = [[0, 0] for _ in range(6)]  # [여, 남]

for _ in range(N):
    S, Y = map(int, input().split())
    cnt[Y-1][S] += 1

ans = 0
for y in range(6):
    for s in range(2):
        c = cnt[y][s]
        if c:
            ans += (c + K - 1) // K

print(ans)