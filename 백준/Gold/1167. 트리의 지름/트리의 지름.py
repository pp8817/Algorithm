import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

V = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    line = list(map(int, input().split()))
    cnt_node = line[0]
    idx = 1
    while line[idx] != -1:
        adj_node, adj_cost = line[idx], line[idx+1]
        graph[cnt_node].append((adj_node, adj_cost))
        idx += 2

def bfs(start):
    visited = [-1 for _ in range(V+1)]
    q = deque()
    q.append(start)
    visited[start] = 0
    max = [0,0]

    while q:
        v = q.popleft()
        for node, dist in graph[v]:
            if visited[node] == -1:
                visited[node] = visited[v] + dist 
                q.append(node)
                if max[0] < visited[node]:
                    max = visited[node], node
    return max

dis, node = bfs(1)
dis, node = bfs(node)
print(dis)