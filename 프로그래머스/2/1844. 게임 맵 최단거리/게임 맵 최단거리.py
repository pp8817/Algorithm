from collections import deque

def solution(maps):
    r, c = len(maps), len(maps[0])
    visited = [[0]*c for _ in range(r)]
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    q = deque([([0,0])])
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()
        
        if (x,y) == (r-1, c-1):
            return visited[x][y]
        
        for i in range(4):
            rx, ry = x+dx[i], y+dy[i]
            if 0<=rx<r and 0<=ry<c and not visited[rx][ry] and maps[rx][ry]:
                visited[rx][ry] = visited[x][y] + 1
                q.append((rx,ry))
                
    return -1 