import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def bfs(point):
    global K
    max_pos = 100001
    visited = [False]*(max_pos)
    visited[point] = True
    q = deque([(point, 0)]) # 출발 지점, 걸리는 시간

    while q:
        current_point, s = q.popleft()

        if current_point == K:
            if s < result[0]:
                result[0] = s
                result[1] = 1
                continue
            elif s == result[0]: # 걸린 시간과 최저 시간이 일치한다면
                result[1] += 1 # 경우의 수 +1
                continue
        
        for np in (current_point+1, current_point-1, current_point*2):
            if 0<=np<max_pos:
                if not visited[np]:
                    q.append((np, s + 1))

        visited[current_point] = True

N, K = map(int, input().split()) # (0 ≤ N,K ≤ 100,000)
result = [float("inf"),0] # 최저 시간, 최저 시간과 동일한 경우의 수
bfs(N)
print(result[0])
print(result[1])