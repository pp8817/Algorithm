import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

INF = int(1e9)
def dijstra(start):
    q = [(0, start)]
    distance = [INF]*(N+1)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue

        for e,t in graph[now]:
            if dist+t < distance[e]:
                distance[e] = dist+t
                heapq.heappush(q, (dist+t, e))

    return distance


N,M,X = map(int, input().split()) # 마을 수, 도로 수, 목적지

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s,e,t = map(int, input().split())
    graph[s].append((e,t))

to_X = [0]*(N+1)
for i in range(1, N+1):
    to_X[i] = dijstra(i)[X]

from_X = dijstra(X)

result = [to_X[i]+from_X[i] for i in range(1, N+1)]
print(max(result))