import sys
input = sys.stdin.readline
from collections import deque

n, m, h = map(int, input().split())
box = []
for i in range(h):
    li = [list(map(int, input().split())) for _ in range(m)]
    box.append(li)
d = [[0,1,0], [0,-1,0], [0,0,1], [0,0,-1], [1,0,0], [-1,0,0]]
res = 0
q = deque()

for z in range(h):
    for i in range(m):
        for j in range(n):
            if box[z][i][j] == 1:
                q.append((z, i, j))

def bfs():
    while q:
        z, x, y = q.popleft()
        for i, j, k in d:
            (dz, dx, dy) = (z+i, x+j, y+k)
            if 0<=dz<h and 0<=dx<m and 0<=dy<n and box[dz][dx][dy]==0:
                box[dz][dx][dy] = box[z][x][y]+1
                q.append((dz, dx, dy))
bfs()

max_t = 0
for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        max_t = max(max_t, max(j))
                
print(max_t-1) ## 처음에 1로 시작하기에 -1