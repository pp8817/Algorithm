import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

d = [[0,0,-1], [0,0,1], [0,1,0], [0,-1,0], [1,0,0], [-1,0,0]]

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    maps = [[] for _ in range(L)]
    for l in range(L):
        for r in range(R):
            row = list(input())
            maps[l].append(row)
            for c in range(C):
                if row[c] == 'S':
                    start = (l, r, c)
                elif row[c] == 'E':
                    end = (l, r, c)
        input()

    q = deque([start])
    visited = [[[0]*C for _ in range(R)] for _ in range(L)]
    visited[start[0]][start[1]][start[2]] = 1

    escaped = False
    while q:
        l, r, c = q.popleft()
        if (l, r, c) == end:
            print(f"Escaped in {visited[l][r][c]-1} minute(s).")
            escaped = True
            break
        
        for dl, dr, dc in d:
            nl, nr, nc = l+dl, r+dr, c+dc
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:
                if not visited[nl][nr][nc] and maps[nl][nr][nc] != "#":
                    visited[nl][nr][nc] = visited[l][r][c] + 1
                    q.append((nl, nr, nc))

    if not escaped:
        print("Trapped!")