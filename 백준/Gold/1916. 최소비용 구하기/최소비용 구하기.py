import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s,e,w = map(int, input().split()) # 출발지, 도착지, 비용
    graph[s].append((e,w))

# 출발 지점, 도착 지점
start_point, end_point = map(int, input().split())

INF = int(1e9)

distance = [INF]*(N+1)
distance[start_point] = 0 # 출발 지점 거리 초기화

q = [(0, start_point)]

while q:
    dist, now = heapq.heappop(q)
    
    if dist > distance[now]: # 현재 노드까지의 거리가 저장되어 있는 값보다 크다면 패스
        continue

    for e,w in graph[now]:
        if dist+w < distance[e]:
            distance[e] = dist+w
            heapq.heappush(q, (dist+w, e))

print(distance[end_point])