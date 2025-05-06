import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    # visited[x][y][c]
        # c == 0: 벽을 아직 안 깬 상태에서 (x, y)에 도달한 경우
        # c == 1: 벽을 한 번 깨고 (x, y)에 도달한 경우
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    q = deque([(0,0,0)])
    visited[0][0][0] = 1

    while q:
        x,y,wall = q.popleft()

        if (x,y) == (N-1, M-1):
            return visited[x][y][wall]
        
        for i in range(4):
            rx, ry = x+dx[i], y+dy[i]
            if 0<=rx<N and 0<=ry<M:
                if map[rx][ry] == 0 and not visited[rx][ry][wall]:
                    visited[rx][ry][wall] = visited[x][y][wall] + 1
                    q.append((rx, ry, wall))
                elif map[rx][ry] == 1 and wall == 0 and not visited[rx][ry][1]:
                    visited[rx][ry][1] = visited[x][y][0] + 1
                    q.append((rx, ry, 1))
    return -1

        
N, M = map(int, input().split())
map = [[] for _ in range(N)]

for i in range(N):
    row = input()
    for num in row:
        map[i].append(int(num))

print(bfs())