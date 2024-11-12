import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

N, M = map(int, input().split())
r,c,d = map(int, input().split()) # d - 0: 북, 1: 동, 2: 남, 3: 서

arr = [list(map(int, input().split())) for _ in range(N)] # 0: 청소 x, 1: 청소 o
visited = [[0]*M for _ in range(N)]
visited[r][c] = 1
ans = 1

while True:
    flag = 0
    for _ in range(4):
        d = (d+3)%4
        nr = r + dx[d]
        nc = c + dy[d]

        if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                ans += 1
                r,c = nr,nc
                flag=1
                break

    if flag == 0:
        if arr[r-dx[d]][c-dy[d]] == 1:
            print(ans)
            break
        else:
            r,c = r-dx[d], c-dy[d]