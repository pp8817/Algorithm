import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def bfs(r,c, col):
    q = deque([(r,c)])

    while q:
        x,y = q.popleft()

        for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
            rx,ry = x+dx, y+dy
            
            if 0<=rx<N and 0<=ry<N:
                if not visited[rx][ry] and ll[rx][ry] == col:
                    q.append((rx,ry))
                    visited[rx][ry] = True

def bfs2(r,c, col):
    q = deque([(r,c)])

    while q:
        x,y = q.popleft()

        for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
            rx,ry = x+dx, y+dy
            
            if 0<=rx<N and 0<=ry<N:
                if not visited[rx][ry] and ll2[rx][ry] == col:
                    q.append((rx,ry))
                    visited[rx][ry] = True

N = int(input())
ll = [[]*N for _ in range(N)]
ll2 = [[]*N for _ in range(N)]
for i in range(N):
    st = input()
    for j in range(N):
        ll[i].append(st[j])
        if st[j] == 'R':
            ll2[i].append('G')
        else:
            ll2[i].append(st[j])

visited = [[False]*N for _ in range(N)]
ans1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j,ll[i][j])
            ans1 += 1

visited = [[False]*N for _ in range(N)]
ans2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs2(i,j,ll2[i][j])
            ans2 += 1
print(ans1, ans2)