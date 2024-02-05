import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append((0,0))
    melt = deque([])
    
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny] = True
                if chz[nx][ny] == 0:
                    q.append((nx, ny))
                elif chz[nx][ny] == 1:
                    melt.append((nx, ny))
    for x, y in melt:
        chz[x][y] = 0
    return len(melt)

n, m = map(int, input().split())
chz = []
cnt = 0
for i in range(n):
    chz.append(list(map(int, input().split())))
    cnt += sum(chz[i])
d = [[0,1], [0,-1], [1,0], [-1,0]]

time = 1

while True:
    visited = [[False] * m for _ in range(n)]
    melCnt = bfs()
    cnt -= melCnt
    
    if cnt == 0:
        print(time)
        print(melCnt)
        break
    time += 1