import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    q = deque([(x,y)])
    picture[x][y] = 0
    count = 1
    
    while q:
        nx, ny = q.popleft()

        for i in range(4):
            rx, ry = nx+dx[i], ny+dy[i]
            if 0<=rx<n and 0<=ry<m and picture[rx][ry]:
                picture[rx][ry] = 0
                count += 1
                q.append((rx,ry))

    return count 
        

n, m = map(int, input().split())
picture = []
pictures = []

for _ in range(n):
    picture.append(list(map(int, input().split())))


for i in range(n):
    for j in range(m):
        if picture[i][j]:
            count = bfs(i,j)
            pictures.append(count)

if pictures:
    print(len(pictures))
    print(max(pictures))
else:
    print(0)
    print(0)