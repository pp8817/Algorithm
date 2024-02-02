import sys
input = sys.stdin.readline
from collections import deque

N, M, T = map(int, input().split())
grid = []
visited = [[0]*(M+1) for _ in range(N+1)]

for _ in range(N):
    grid.append(list(map(int, input().split())))

a, b = 0, 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 2:
            a, b = i, j
            break

d = [[0,1], [0,-1], [1,0], [-1,0]]

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    gram = 10001

    while q:
        x, y = q.popleft()
        
        if (x, y) == (N-1, M-1):
            return min(visited[x][y]-1, gram)
        if grid[x][y] == 2:
            gram = visited[x][y]-1 + N-1-x + M-1-y
    
        for dx, dy in d:
            r, c = x+dx, y+dy
            
            if 0<=r<N and 0<=c<M and visited[r][c]==0:
                if grid[r][c] == 0 or grid[r][c] == 2:
                    visited[r][c] = visited[x][y] + 1
                    q.append((r, c))
    return gram

res = bfs()
if res > T:
    print("Fail")
else:
    print(res)