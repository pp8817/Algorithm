import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

R, C = map(int, input().split())
miro = []
fire_q = deque()
jihoon_q = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 입력 및 초기 위치 설정
for i in range(R):
    row = list(input())
    miro.append(row)
    for j in range(C):
        if row[j] == 'F':
            fire_q.append((i, j))
        elif row[j] == 'J':
            jihoon_start = (i, j)

# 각 위치에 불이 도달하는 시간 저장
fire_time = [[-1]*C for _ in range(R)]
for x, y in fire_q:
    fire_time[x][y] = 0

while fire_q:
    x, y = fire_q.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < R and 0 <= ny < C:
            if miro[nx][ny] != '#' and fire_time[nx][ny] == -1:
                fire_time[nx][ny] = fire_time[x][y] + 1
                fire_q.append((nx, ny))

# 지훈이 BFS
jihoon_time = [[-1]*C for _ in range(R)]
sr, sc = jihoon_start
jihoon_q.append((sr, sc))
jihoon_time[sr][sc] = 0

while jihoon_q:
    x, y = jihoon_q.popleft()

    if x == 0 or x == R-1 or y == 0 or y == C-1:
        print(jihoon_time[x][y] + 1)
        sys.exit()

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < R and 0 <= ny < C:
            if miro[nx][ny] != '#' and jihoon_time[nx][ny] == -1:
                next_time = jihoon_time[x][y] + 1
                if fire_time[nx][ny] == -1 or next_time < fire_time[nx][ny]:
                    jihoon_time[nx][ny] = next_time
                    jihoon_q.append((nx, ny))

print("IMPOSSIBLE")