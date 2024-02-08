import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
m = 100001
visited = [-1]*100001
visited[N] = 0

def bfs(v):
    q = deque()
    q.append(v)
    
    while q:
        w = q.popleft()
        if w == K:
            print(visited[w])
            break
        if 0<=w*2<m and visited[2*w] == -1:
            visited[w*2] = visited[w]
            q.append(2*w)
        if 0<=w-1<m and visited[w-1] == -1:
            visited[w-1] = visited[w]+1
            q.append(w-1)
        if 0<=w+1<m and visited[w+1] == -1:
            visited[w+1] = visited[w]+1
            q.append(w+1)
bfs(N)  