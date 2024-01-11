import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(start):
  visited[start] = True
  
  for w in graph[start]:
    if not visited[w]:
      dfs(w)
  

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited=[False]*(N+1)


for _ in range(M):
  a, b = map(int, input().split())
  graph[a] += [b]
  graph[b] += [a]
  
dfs(1)
print(sum(visited)-1)