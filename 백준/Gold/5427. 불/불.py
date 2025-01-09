import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

d = [[0,1], [1,0], [0,-1], [-1,0]]

def burn():
    for _ in range(len(fire)):
        x, y = fire.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            
            if 0 <= nx < h and 0 <= ny < w:
                if arr[nx][ny] != "#" and arr[nx][ny] != '*':
                    arr[nx][ny] = "*"
                    fire.append((nx,ny))

def move():
    isgo = False
    for _ in range(len(start)):
        x,y = start.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and arr[nx][ny] != '#' and arr[nx][ny] != '*':
                    isgo = True
                    visited[nx][ny] = visited[x][y] + 1
                    start.append((nx,ny))
            else:
                return visited[x][y]
    if not isgo:
        return "IMPOSSIBLE"

T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    arr = []
    fire = deque()
    start = deque()
    for i in range(h):
        arr.append(list(input().strip()))
        for j in range(w):
            if arr[i][j] == '*':
                fire.append((i,j))
            elif arr[i][j] == '@':
                start.append((i,j))
    visited = [[0]*w for _ in range(h)]
    visited[start[0][0]][start[0][1]] = 1

    result = 0
    while True:
        burn()
        result = move()
        if result:
            break
    print(result)