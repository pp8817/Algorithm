import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

# 최단 경로 -> 우선 순위 큐, 다익스트라 알고리즘

def dijkstra(start_point):
    dist = [float('INF') for _ in range(V)] # 각 정점까지의 최단 경로를 담을 리스트
    dist[start_point] = 0
    pq = [(0, start_point)]

    while pq:
        current_dist, n = heapq.heappop(pq)

        if current_dist > dist[n]:
            continue

        for (v, d) in graph[n]:
            distance = d + current_dist
            if dist[v] > distance:
                dist[v] = distance
                heapq.heappush(pq, (distance, v))

    return dist

V, E = map(int, input().split())

start_point = int(input())-1

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u-1].append((v-1,w))

dist = dijkstra(start_point)

for i in dist:
    if i == float("INF"):
        print("INF")
        continue
    print(i)