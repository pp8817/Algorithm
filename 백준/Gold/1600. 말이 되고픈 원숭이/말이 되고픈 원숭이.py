import sys
input = sys.stdin.readline
from collections import deque

chess = [[-2, 1], [-1, 2], [1,2], [2,1], [-2,-1],[-1,-2], [1,-2], [2,-1]]
d = [[0,1], [1,0], [0,-1], [-1,0]]

def bfs(n):
    
    q = deque()
    q.append((0,0,n))
    visited = [[[0]*(n+1) for _ in range(w)] for _ in range(h)]
    
    while q:
        x, y, K = q.popleft() #열의 위치, 행의 위치, 
        
        if x==h-1 and y == w-1:
            return visited[x][y][K]
        if K>0:
            for dx, dy in chess:
                nx, ny = x+dx, y+dy
                if 0<=nx<h and 0<=ny<w:
                    if grid[nx][ny] != 1 and visited[nx][ny][K-1] == 0:
                        visited[nx][ny][K-1] = visited[x][y][K]+1
                        q.append((nx,ny,K-1))
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0<=nx<h and 0<=ny<w:
                if grid[nx][ny] != 1 and visited[nx][ny][K] == 0:
                    visited[nx][ny][K] = visited[x][y][K]+1
                    q.append((nx,ny,K))
    return -1

K = int(input())
w,h = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]

result = bfs(K)  
print(result)