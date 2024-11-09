import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

M, N, K = map(int, input().split())
board = [[0]*N for _ in range(M)]
for _ in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(M-y2, M-y1):
        for j in range(x1,x2):
            board[i][j] = 1

def bfs(r,c):
    q = deque()
    q.append((r,c))
    board[r][c] = 1
    size = 1

    while q:
        x,y = q.popleft()

        for rx,ry in [[0,1], [0,-1], [1,0], [-1,0]]:
            nx, ny = x+rx, y+ry

            if 0<=nx<M and 0<=ny<N and not board[nx][ny]:
                size += 1
                board[nx][ny] = 1
                q.append((nx,ny))
    ans.append(size)

ans = []         
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            count = bfs(i,j)

ans.sort()
print(len(ans))
print(*ans)
