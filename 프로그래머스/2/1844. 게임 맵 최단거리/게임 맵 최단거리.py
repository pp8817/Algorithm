from collections import deque

def solution(maps):
    answer = 0
    R,C = len(maps), len(maps[0])
    
    def bfs():
        while q:
            x,y,c = q.popleft()
            
            if (x,y) == (R-1,C-1):
                return c
    
            for rx,ry in [(0,1), (0,-1), (1,0), (-1,0)]:
                nx,ny = x+rx, y+ry

                if 0<=nx<R and 0<=ny<C and not visited[nx][ny]:
                    if maps[nx][ny] == 1:
                        visited[nx][ny] = True
                        q.append((nx,ny,c+1))
        return -1
    q = deque([])
    q.append((0,0,1))
    visited = [[False]*C for _ in range(R)]
    
    count = bfs()
    return count