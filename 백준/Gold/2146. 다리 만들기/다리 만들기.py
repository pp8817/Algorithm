import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

d = [(-1,0), (1,0), (0,-1), (0,1)]

def label_islands(maps, N):
    visited = [[False]*N for _ in range(N)]
    island_id = 2 

    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1 and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                maps[i][j] = island_id

                while q:
                    x, y = q.popleft()
                    for dx, dy in d:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            if maps[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                maps[nx][ny] = island_id
                                q.append((nx, ny))

                island_id += 1
    return maps, island_id - 1 

def get_border_cells(maps, N, island_id):
    borders = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == island_id:
                for dx, dy in d:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < N and 0 <= nj < N:
                        if maps[ni][nj] == 0:
                            borders.append((i, j))
                            break
    return borders

def bridge_length_bfs(r, c, label, maps, N):
    visited = [[0]*N for _ in range(N)]
    q = deque([(r, c)])

    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if maps[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                elif maps[nx][ny] != label:
                    return visited[x][y]
    return float('inf')

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

maps, island_cnt = label_islands(maps, N)

min_dist = float('inf')

for island_id in range(2, island_cnt + 1):
    border_cells = get_border_cells(maps, N, island_id)
    for x, y in border_cells:
        dist = bridge_length_bfs(x, y, island_id, maps, N)
        min_dist = min(min_dist, dist)

print(min_dist)