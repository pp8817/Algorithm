import sys
input = sys.stdin.readline
from collections import deque

N, L, R = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
d = [[-1,0], [1,0], [0,-1], [0,1]]

def bfs(r, c):
    q = deque()
    temp = []
    q.append((r, c))
    temp.append((r, c))
    
    while q:
        x, y = q.popleft()
        
        for i, j in d:
            (dx, dy) = (x+i, y+j)
            if 0<=dx<N and 0<=dy<N and visited[dx][dy]==0:
                if L<=abs(g[dx][dy]-g[x][y])<=R:
                    visited[dx][dy] = 1
                    q.append((dx, dy))
                    temp.append((dx, dy))
    return temp

res = 0
while True:
    visited = [[0]*(N+1) for _ in range(N+1)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                visited[i][j] = 1
                country = bfs(i, j)
                
                if len(country) > 1:
                    flag=1
                    
                    number = sum([g[i][j] for i, j in country]) // len(country)
                    
                    for x, y in country:
                        g[x][y] = number
    if flag == 0:
        break
    res += 1
print(res)