import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for i in range(N):
    arr = input()
    for a in arr:
        graph[i].append(int(a))

visited = [[0]*M for _ in range(N)]
q = deque([(0,0)])
visited[0][0] = 1

while q:
    r,c = q.popleft()

    if (r,c) == (N-1,M-1):
        print(visited[r][c])
        break

    for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
        nx,ny = r+dx, c+dy
        if 0<=nx<N and 0<=ny<M: 
            if visited[nx][ny] == 0 and graph[r][c] == 1:
                visited[nx][ny] = visited[r][c] + 1
                q.append((nx,ny))