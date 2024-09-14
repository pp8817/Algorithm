import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

# 가까운 먹이 탐색
def bfs(i, j):
    global N
    q = deque([(i,j)])
    visited = [[0]*N for _ in range(N)]
    visited[i][j] = 1
    dist_info = [] # 거리, 행, 열
    while q:
        cx, cy = q.popleft()

        for nx, ny in d:
            rx, ry = cx+nx, cy+ny

            if 0<=rx<N and 0<=ry<N and visited[rx][ry] == 0:
                if box[i][j] > box[rx][ry] and box[rx][ry]:
                    visited[rx][ry] = visited[cx][cy] + 1
                    dist_info.append((visited[rx][ry]-1, rx,ry))
                elif box[i][j] == box[rx][ry]:
                    visited[rx][ry] = visited[cx][cy] + 1
                    q.append((rx,ry))
                elif box[rx][ry] == 0:
                    visited[rx][ry] = visited[cx][cy] + 1
                    q.append((rx,ry))
    return sorted(dist_info, key = lambda x: (x[0], x[1], x[2]))
                


N = int(input())
box = [] # NxN 크기의 공간 리스트

i,j = 0, 0
for row in range(N):
    li = list(map(int, input().split()))
    box.append(li)
    for col in range(N):
        if li[col] == 9:
            i, j = row, col

d = [[-1,0], [0,1], [1,0], [0,-1]]

size = [2,0]
time = 0
while True:
    box[i][j] = size[0]
    dist_info = deque(bfs(i,j))
    if not dist_info:
        break

    step, x, y = dist_info.popleft()
    time += step
    size[1] += 1

    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0
    box[i][j] = 0
    i, j = x, y

print(time)