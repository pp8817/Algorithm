from collections import deque

N, M = map(int, input().split())
d = [[0,1], [0,-1], [1,0], [-1,0]]
grid = [list(map(int, input())) for _ in range(N)]

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

def bfs():
    q = deque([(0,0,0)])
    while q:
        x, y, k = q.popleft()
        
        if (x,y) == (N-1, M-1):
            return visited[x][y][k]
        
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M:
                if grid[nx][ny] == 1 and k == 0:
                    visited[nx][ny][1] = visited[x][y][0] +1
                    q.append((nx,ny,1))
                elif (not grid[nx][ny]) and (not visited[nx][ny][k]):
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    q.append((nx,ny,k))                
    return -1

print(bfs())    