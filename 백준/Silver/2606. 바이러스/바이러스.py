import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
v = int(input())
graph = [[] for i in range(n+1)] # 그래프 초기화

visited = [0]*(n+1)

for i in range(v): #그래프 생성
    a, b = map(int, input().split())
    graph[a] += [b] # a에 b 연결
    graph[b] += [a] # b에 a 연결 - 양방향

def dfs(v):
    visited[v] = True
    for nx in graph[v]:
        if not visited[nx]:
            dfs(nx)
dfs(1) #시작 위치
print(sum(visited)-1)