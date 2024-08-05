import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def bfs():
    q = deque()
    q.append((0,0))
    visited = [[0]*M for _ in range(N)]

    while q:
        r,c = q.popleft()

        for x,y in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = r+x, c+y
            if 0<=nx<N and 0<=ny<M:
                if (visited[nx][ny] == 0) and (box[nx][ny]==0):
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                elif box[nx][ny] == 1:
                    visited[nx][ny] += 1

                    if visited[nx][ny] == 2:
                        box[nx][ny] = 0


N, M = map(int, input().split())
box = []
for i in range(N):
    box.append(list(map(int, input().split())))

count = 0
a = True
while a:
    bfs()
    count += 1
    a = False
    for b in box:
        if 1 in b:
            a = True
            break

print(count)