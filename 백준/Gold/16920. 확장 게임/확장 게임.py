import sys
from collections import deque

input = sys.stdin.readline
N, M, P = map(int, input().split())
S = list(map(int, input().split()))

board = [list(input().strip()) for _ in range(N)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

qs = [deque() for _ in range(P)]
owned = [0]*P

for i in range(N):
    for j in range(M):
        ch = board[i][j]
        if ch.isdigit():
            pid = int(ch)-1
            qs[pid].append((i,j))
            owned[pid] += 1

active = True
while active:
    active = False
    for pid in range(P):
        if not qs[pid]:
            continue
        step = S[pid]
        for _ in range(step):
            if not qs[pid]:
                break
            active = True
            for _ in range(len(qs[pid])):
                y, x = qs[pid].popleft()
                for dy, dx in dirs:
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == '.':
                        board[ny][nx] = str(pid+1)
                        owned[pid] += 1
                        qs[pid].append((ny, nx))

print(*owned)