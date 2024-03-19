import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def bfs(v):
    global visited
    q = deque([v])
    visited[v] = 1

    while q:
        n = q.popleft()

        for d in graph[n]:
            if not visited[d]:
                q.append(d)
                visited[d] = visited[n] + 1

# N (2 ≤ N ≤ 100), M (1 ≤ M ≤ 5,000)
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]


for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

result = []
for i in range(1, N+1):
    visited = [0]*(N+1)
    bfs(i)
    result.append(sum(visited))
print(result.index(min(result))+1)