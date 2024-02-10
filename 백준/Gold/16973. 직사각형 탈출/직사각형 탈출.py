import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, input().split())

d = [[0,1], [0,-1], [1,0], [-1,0]]
visited = [[0]*M for _ in range(N)]

q = deque()

q.append((Sr-1, Sc-1, 0))
point = (Fr-1, Fc-1)

def bfs():
    
    while q:
        r,c, cnt = q.popleft()
        if (r,c) == point:
            print(cnt)
            return 
        
        for nx, ny in d:
            x,y = r+nx, c+ny
            if 0<=x<N and 0<=y<M and 0<= x+H-1<N and 0<=y+W-1<M:
                if visited[x][y] == 0:
                    if check(x,y):
                        visited[x][y] = 1
                        q.append((x,y, cnt+1))
                
    print(-1)
    return 

walls = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            walls.append((i, j))
            
def check(x, y):
    for r, c in walls:
        if x<=r<x+H and y <= c <y+W:
            return False
    return True
    
bfs()