import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

def dfs(graph, v):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i)
            
def bfs(graph, v):
    q = deque([v])
    visited[v] = True
    
    while q:
        node = q.popleft()
        
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
        print(node, end=' ')

N, M, V = map(int, input().split())

graph = [[] for i in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

for i in range(1, N+1):
    graph[i].sort()

visited = [False] * (N+1)
dfs(graph, V)
print()
visited = [False] * (N+1)
bfs(graph, V)