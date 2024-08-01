import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

INF = int(1e9)

def dijkstra(start):
    dist = [INF]*(N+1)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        current_dist, node = heapq.heappop(q)

        if dist[node] < current_dist:
            continue

        for v, distance in graph[node]:
            cost = distance + dist[node]

            if dist[v] > cost:
                heapq.heappush(q, (cost, v))
                dist[v] = cost

    return dist


N = int(input())
M = int(input())

graph = [[]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a] += [(b,c)]

s, point = map(int, input().split())

result = dijkstra(s)
print(result[point])