import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(m)]
visited = [[False]*n for _ in range(m)]
d = [[1,0], [-1,0], [0,1], [0,-1]]
res = 0
q = deque()
for i in range(m):
    for j in range(n):
        if box[i][j] == 1:
            q.append((i,j))

def bfs():
    while q:
        r, c = q.popleft()
        for (dx, dy) in d:
            (x, y) = (dx+r, dy+c)
            if (0<=x<m) and (0<=y<n) and box[x][y]==0:
                box[x][y] = box[r][c] + 1
                q.append((x,y))
bfs()
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)