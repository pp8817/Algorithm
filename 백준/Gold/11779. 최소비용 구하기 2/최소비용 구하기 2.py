import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

INF = int(1e9)

def sol(N,start,point):
    dist = [(INF, []) for _ in range(N+1)]
    dist[start] = (0, [start])

    l = []
    heapq.heappush(l, [0, start]) #distance, city

    while l:
        current_dist, n = heapq.heappop(l)

        if current_dist > dist[n][0]:
            continue

        for nn, distance in bus[n]:
            d = current_dist + distance
            if dist[nn][0] > d:
                dist[nn] = (d, dist[n][1]+[nn])
                heapq.heappush(l, (d, nn))
 
    return dist[point]


n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

bus = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    bus[s].append((e,c))

start, point = map(int, input().split())
result = sol(n, start, point)

print(result[0])
print(len(result[1]))
print(' '.join(map(str, result[1])))