import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

def dfs(v):
    visited[v] = True

    for w in graph[v]:
        if not visited[w]:
            dic[w] = v
            dfs(w)

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    s,t = map(int, input().split())
    graph[s].append(t)
    graph[t].append(s)

visited = [False]*(N+1)

dic = {i:0 for i in range(1,N+1)}
dfs(1)
for i in range(2, N+1):
    print(dic[i])