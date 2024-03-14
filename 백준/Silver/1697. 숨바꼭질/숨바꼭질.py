import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
e = 100001
visited = [False]*e

q = deque()
q.append((N, 0))

while q:
    x, c = q.popleft()
    if x == K:
        print(c)
        break
    for i in [1, -1]:
        nx = x + i
        if 0<= nx < e and not visited[nx]:
            visited[nx] = visited[x]+1
            q.append((nx, c+1))
    if 0<= 2*x < e and not visited[2*x]:
        visited[2*x] = visited[x]+1
        q.append((2*x, c+1))
