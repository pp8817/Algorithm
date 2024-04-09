import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

# O는 빈 공간, X는 벽, I는 도연이, P는 사람

N, M = map(int, input().split())
campus = [[] for _ in range(N)]
visited = [[False] * M for _ in range(N)]
d = [[1,0], [-1,0], [0,1], [0,-1]]
q = deque()

for i in range(N):
    l = input()
    for j in range(M):
        inf = l[j]
        campus[i].append(inf)
        if inf == 'I':
            q.append((i,j))
            visited[i][j] = True

count = 0
while q:
    (x,y) = q.popleft()

    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            if campus[nx][ny] == 'O':
                visited[nx][ny] = True
                q.append((nx,ny))
            elif campus[nx][ny] == 'P':
                count += 1
                visited[nx][ny] = True
                q.append((nx,ny))
if not count:
    print("TT")
else:
    print(count)