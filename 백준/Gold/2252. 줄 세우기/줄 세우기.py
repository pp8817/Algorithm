import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
in_degree = [0]*(N+1)
q = deque()
for _ in range(M):
    A, B = map(int, input().split()) # A가 B 앞에 서야 한다.
    graph[A].append(B)
    in_degree[B] += 1

for i in range(1, N+1):
    if in_degree[i] == 0:
        q.append(i)

result = []
while q:
    node = q.popleft()
    result.append(node)

    for next_node in graph[node]:
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            q.append(next_node)
print(*result)