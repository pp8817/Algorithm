import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

d = [[1,0], [-1,0], [0,1], [0,-1]]

def bfs(r, c, grid, visited):
    q = deque([(r,c)])
    visited[r][c] = True

    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy

            if 0<=nx<N and 0<=ny<M:
                if grid[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    grid = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    for _ in range(K):
        c, r = map(int, input().split()) # 가로, 세로
        grid[r][c] = 1
    
    index = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and not visited[i][j]:
                bfs(i,j, grid, visited)
                index += 1
    print(index)