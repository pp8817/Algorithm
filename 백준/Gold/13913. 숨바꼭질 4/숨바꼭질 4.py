import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, K = map(int, input().split())
MAX = 100000

route = [-1] * (MAX + 1)
visited = [False] * (MAX + 1)

q = deque([(N, 0)])
visited[N] = True

while q:
    now, t = q.popleft()

    if now == K:
        print(t)
        break

    for nxt in (now - 1, now + 1, now * 2):
        if 0 <= nxt <= MAX and not visited[nxt]:
            visited[nxt] = True
            route[nxt] = now
            q.append((nxt, t + 1))

path = []
cur = K
while cur != -1:
    path.append(cur)
    cur = route[cur]

print(*reversed(path))