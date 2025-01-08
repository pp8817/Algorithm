import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

T = int(input())

d = [[-2, -1], [-1,-2], [1, -2], [2, -1], [-2,1], [-1, 2], [1, 2], [2, 1]]

for _ in range(T):
    N = int(input())
    start_x, start_y = map(int, input().split())
    point_x, point_y = map(int, input().split())

    visited = [[0]*N for _ in range(N)]
    visited[start_x][start_y] = 1

    q = deque([(start_x, start_y)])

    while q:
        x, y = q.popleft()

        if (x,y) == (point_x, point_y):
            print(visited[x][y]-1)
            break

        for dx, dy in d:
            rx,ry = x+dx, y+dy
            if 0<=rx<N and 0<=ry<N and not visited[rx][ry]:
                visited[rx][ry] = visited[x][y] + 1
                q.append((rx,ry))