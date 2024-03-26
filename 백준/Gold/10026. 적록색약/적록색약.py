import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def bfs(r,c, color):
    q = deque()
    q.append((r,c))
    visited[r][c] = True

    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx, ny = x+dx, y+dy

            if 0<=nx<N and 0<=ny<N:
                if not visited[nx][ny] and grid[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return grid[r][c]

N = int(input())
grid = [list(input()) for _ in range(N)]
d = [[1,0], [-1,0], [0,1], [0,-1]]


visited = [[False]*N for _ in range(N)]
cnt1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color = bfs(i,j, grid[i][j])
            cnt1+=1

# 적록색약인 경우
dic = {"R":0, "G":0}
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'
visited = [[0] * N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j, grid[i][j])
            cnt2 += 1
print(cnt1, cnt2)