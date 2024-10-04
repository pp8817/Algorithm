import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def dfs(start):
    visited[start] = True
    print(start, end = ' ')

    for v in graph[start]:
        if not visited[v]:
            dfs(v)

def bfs(start):
    visited[start] = True
    q = deque([start])

    while q:
        node = q.popleft()

        for v in graph[node]:
            if not visited[v]:
                q.append(v)
                visited[v] = True
        print(node, end = ' ')




N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s,t = map(int, input().split())
    graph[s].append(t)
    graph[t].append(s)

for i in range(1,N+1):
    graph[i].sort()

visited = [False]*(N+1)
dfs(V)
print()
visited = [False]*(N+1)
bfs(V)