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
            cost = current_dist + distance

            if dist[v] > cost:
                dist[v] = cost
                heapq.heappush(q, (cost, v))

    return dist

N, E = map(int, input().split()) # 정점, 간선 개수

graph = [[]*(N+1) for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a] += [(b,c)]
    graph[b] += [(a,c)]

v1,v2 = map(int, input().split()) # 반드시 거쳐야 하는 두 개의 정점 번호

origin_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

v1_path = origin_dist[v1] + v1_dist[v2] + v2_dist[N]
v2_path = origin_dist[v2] + v2_dist[v1] + v1_dist[N]

result = min(v1_path, v2_path)
print(result if result < INF else -1)