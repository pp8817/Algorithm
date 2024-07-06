import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

def dijkstra(start):
    distances = [float('inf')] * (N + 1)
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, node = heapq.heappop(pq)
        
        if current_dist > distances[node]:
            continue
        
        for (v, t) in road[node]:
            distance = current_dist + t
            if distance < distances[v]: # distance가 기존 v까지의 거리보다 적다면
                distances[v] = distance # distances[v]를 distance로 변경
                heapq.heappush(pq, (distance, v))
    
    return distances

N, M, X = map(int, input().split())
road = [[] for _ in range(N + 1)]

for i in range(M):
    s, e, t = map(int, input().split())
    road[s].append((e, t))

# 각 마을에서 X로 가는 최단 거리
to_X = [0] * (N + 1)
for i in range(1, N + 1):
    distances = dijkstra(i)
    to_X[i] = distances[X]

# X에서 각 마을로 가는 최단 거리
from_X = dijkstra(X)

# 결과 계산
result = [to_X[i] + from_X[i] for i in range(1, N + 1)]
print(max(result))
