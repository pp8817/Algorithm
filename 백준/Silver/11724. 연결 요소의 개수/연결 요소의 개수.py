import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

def dfs(n):
    visited[n]=True

    for d in graph[n]:
        if not visited[d]:
            dfs(d)


# (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
N, M = map(int, input().split())

# (1 ≤ u, v ≤ N, u ≠ v)
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)