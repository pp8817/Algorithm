import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def bfs():
    q = deque([(0, 0, 0, 1)])
    visited = [[[False]*(K+1) for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = True

    while q:
        x, y, b, d = q.popleft()
        if x == N-1 and y == M-1:
            return d

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and not visited[nx][ny][b]:
                    visited[nx][ny][b] = True
                    q.append((nx, ny, b, d+1))
                elif graph[nx][ny] == 1 and b < K and not visited[nx][ny][b+1]:
                    visited[nx][ny][b+1] = True
                    q.append((nx, ny, b+1, d+1))
    return -1

N, M, K = map(int, input().split())

dx = [0,0,1,-1]
dy = [-1,1,0,0]
graph = [list(map(int, input().rstrip())) for _ in range(N)]

print(bfs())