from collections import deque
def solution(board):
    d = [[0,1], [0,-1], [1,0], [-1,0]]
    W, H = len(board), len(board[0])
    sx, sy, px, py = 0,0,0,0
    t = set()
    
    for i in range(W):
        for j in range(H):
            if board[i][j] == "R":
                sx, sy = i, j
            elif board[i][j] == "G":
                px, py = i,j
            elif board[i][j] == "D":
                t.add((i,j))
                
    def bfs(r, c):
        q = deque([(r,c,0)])
        visited = set()
        
        while q:
            x, y, k = q.popleft()
            
            if (x,y) == (px,py):
                return k
            
            if (x,y) in visited:
                continue
            visited.add((x,y))
            
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if 0<=nx<W and 0<=ny<H and board[nx][ny] != "D":
                    while True:
                        a, b = nx, ny
                        nx += dx
                        ny += dy
                        if ((nx,ny) in t) or nx<0 or nx>=W or ny<0 or ny>=H:
                            q.append((a, b, k+1))
                            break
        return -1
    
    return bfs(sx, sy)
        