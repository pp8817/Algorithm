from collections import deque
def solution(maps):
    answer = 0
    
    x, y = 0, 0
    lx, ly = 0, 0
    ex, ey = 0, 0
    
    W, H = len(maps), len(maps[0])
    
    for i in range(W):
        for j in range(H):
            if maps[i][j] == "S":
                x, y = i, j
            elif maps[i][j] == "E":
                ex, ey = i, j
            elif maps[i][j] == "L":
                lx, ly = i, j
    
    K1 = bfs(x, y, lx, ly, maps, W, H)
    if K1 == -1:
        return -1
    answer += K1
    K2 = bfs(lx, ly, ex, ey, maps, W, H)
    if K2 == -1:
        return -1
    answer += K2

    return answer

def bfs(x, y, point_x, point_y, maps, W, H):
    d = [[0,1], [0,-1], [1,0], [-1,0]]
    visited = [[False]*H for _ in range(W)]
    
    q = deque([(x,y,0)])
    
    while q:
        r, c, k = q.popleft()
        
        if (r, c) == (point_x, point_y):
            return k
        
        for dx, dy in d:
            nx, ny = r+dx, c+dy
            
            if 0<=nx<W and 0<=ny<H:
                if maps[nx][ny] != "X" and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, k+1))
    return -1