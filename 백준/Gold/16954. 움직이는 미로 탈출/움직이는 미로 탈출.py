import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**5)
from collections import deque

def bfs():
    q = deque([(7,0)])
    cnt = 0
    
    while q:
        for _ in range(len(q)):
            (x,y) = q.popleft()

            if [x,y] in wall:
                continue

            if x==0 or cnt == 9:
                return 1

            for dx, dy in d:
                nx, ny = x+dx, y+dy

                if 0<=nx<8 and 0<=ny<8:
                    if [nx,ny] not in wall:
                        q.append((nx,ny))
        wall_down()
        cnt += 1
    return 0

def wall_down():
    for i in range(len(wall)):
        wall[i] = [wall[i][0]+1, wall[i][1]]
            
n, m = 8,8
grid = [[] for _ in range(8)]
wall = []
d = [[0, 0], [1, 0], [-1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

for i in range(8):
    a = input()
    for j in range(8):
        grid[i].append(".")
        if a[j] == "#":
            wall.append([i,j])
    
if len(wall) == 0:
    print(1)
else:
    print(bfs())