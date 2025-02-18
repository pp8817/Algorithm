import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

V, E = map(int, input().split()) # 정점의 개수, 간선의 개수
K = int(input()) # 시작 정점
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

distance = [float('INF')]*(V+1)
distance[K] = 0

q = []
heapq.heappush(q, (0, K))

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist: # distance에 저장된 값이 현재 노드까지의 값(dis)보다 작다면 이미 방문한 노드이기 때문에 패스 
        continue

    for v,w in graph[now]:
        if dist+w < distance[v]: # 기존에 입력되어 있는 값보다 작다면
            distance[v] = dist+w
            heapq.heappush(q, (dist+w, v))


# i번째 줄에 i번 정점으로의 최단 경로값 출력, 시작점은 0
for i in distance[1:]:
    if i == float('INF'):
        print('INF')
        continue
    print(i)