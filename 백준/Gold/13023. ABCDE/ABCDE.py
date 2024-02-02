import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

g = [[] for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    g[a] += [b]
    g[b] += [a]

def dfs(v, visited, cnt):
    global answer
    
    visited[v] = True
    if cnt == 4:
        answer = True
        return
    for i in g[v]:
        if not visited[i]:
            dfs(i, visited, cnt+1)
    visited[v] = False
        

flag=0

for i in range(N):
    answer=False
    
    visited = [False]*N
    dfs(i, visited, 0)
    if answer:
        print(1)
        break
else:
    print(0)