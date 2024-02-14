import sys
input = sys.stdin.readline
from collections import deque

d = [[-1,0],[1,0],[0,1],[0,-1]]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    visited[x][y] = True

    while queue:
        r,c = queue.popleft()
        for dx, dy in d:
            dr, dc = r+dx, c+dy

            if (0<=dr<n) and (0<=dc<m):
                if graph[dr][dc] == 0:
                    visited[r][c] += 1

                if not visited[dr][dc] and graph[dr][dc] != 0 :
                    queue.append([dr,dc])
                    visited[dr][dc] = True


n , m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]


time = 0
while True:
    count = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j]!=0:
                bfs(i,j)
                count +=1

    for i in range(n):
        for j in range(m):
            if visited[i][j] :
                graph[i][j] -= (visited[i][j]-1)
                if graph[i][j] < 0: graph[i][j] = 0

    time += 1
    if count == 0:
        print(0)
        exit()
    if count >=2 :
        break

print(time-1)