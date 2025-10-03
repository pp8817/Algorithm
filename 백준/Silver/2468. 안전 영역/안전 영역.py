from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
areas = [list(map(int, input().split())) for _ in range(N)]

max_height = max(map(max, areas))
answer = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(r, c, h, visited):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and areas[nx][ny] > h:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

for h in range(0, max_height):
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and areas[i][j] > h:
                bfs(i, j, h, visited)
                cnt += 1
    answer = max(answer, cnt)

print(answer)