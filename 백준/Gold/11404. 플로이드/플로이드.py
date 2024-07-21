import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

INF = float('inf')

# 도시의 개수와 버스의 개수 입력
n = int(input())
m = int(input())

# 초기화: 모든 비용을 무한대로 설정
dist = [[INF] * n for _ in range(n)]

# 자기 자신으로 가는 비용은 0으로 설정
for i in range(n):
    dist[i][i] = 0

# 버스 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], c)  # 같은 노선에 대해 더 작은 비용 저장

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()

