import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def bfs(v):
    q = deque([v])
    visited = [False]*(N+1)
    visited[v] = True
    count = 0
    
    while q:
        node = q.popleft()
        
        for w in graph[node]:
            if not visited[w]:
                visited[w] = True
                count+=1
                q.append(w)
    return count
                

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

ans = []

for i in range(1 ,N+1):
    ans.append(bfs(i))
    
maxCnt = max(ans)

for i in range(len(ans)):
    if maxCnt == ans[i]:
        print(i+1)