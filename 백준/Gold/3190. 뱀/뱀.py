import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N = int(input())
K = int(input())
board = [[0]*(N) for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 2

info = {}
l = int(input())
for _ in range(l):# 뱀의 방향변환정보 (초, 방향 L:왼쪽 D:오른쪽)
    sec, direct = input().split()
    info[int(sec)] = direct

time = 0
dx=[0,1,0,-1]
dy=[1,0,-1,0]
d = 0
x,y = 0,0
board[0][0] = 1 # 0: 아무것도 없는 상태, 1: 뱀이 위치한 장소, 2: 사과 위치
q = deque([(0,0)])

while True:
    nx, ny = x+dx[d], y+dy[d]
    
    if 0<=nx<N and 0<=ny<N and (nx,ny) not in q:
        if board[nx][ny] != 2:
            r,c = q.popleft()
            board[r][c] = 0
        x,y = nx,ny
        board[x][y] = 1
        q.append((x,y))
        time += 1

        if time in info.keys():
            if info[time] == "D":
                d = (d+1)%4
            else:
                d = (d-1)%4
    else:
        break
print(time+1)