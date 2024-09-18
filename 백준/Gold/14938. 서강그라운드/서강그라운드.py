import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

n, m, r = map(int, input().split()) # 지역 개수, 수색 범위, 길의 개수
t = list(map(int, input().split())) # 각 지역의 아이템 수

road = [[] for _ in range(n+1)]
for _ in range(r):
    a,b,l = map(int, input().split())
    road[a].append((b,l))
    road[b].append((a,l))


def dijstra(start):
    que = []
    heapq.heappush(que, (0, start))
    D[start] = 0

    while que:
        dist, now = heapq.heappop(que)
        if D[now] < dist:
            continue

        for b,l in road[now]:
            cost = dist+l
            if cost <= m:
                D[b] = cost
                heapq.heappush(que, (cost,b))

    


INF = int(1e9)
ans = 0
for i in range(n+1):
    D = [INF]*(n+1) # i부터 각 위치까지 걸리는 거리를 나타내는 리스트
    dijstra(i)
    tmp = 0 # 총 아이템 수
    for d in range(n+1):
        if D[d]<=m:
            tmp += t[d-1]
    ans = max(ans, tmp)

print(ans)