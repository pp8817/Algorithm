import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

T = int(input())

for _ in range(T):
    N, K = map(int, input().split()) # 건물 갯수, 건물 건설 규칙 수
    t = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N + 1) # 진입 차수 계산
    for _ in range(K):
        x,y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    dp = [0]*(N+1)
    q = deque()
    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = t[i]
    
    while q:
        n = q.popleft()

        for v in graph[n]:
            dp[v] = max(dp[v], dp[n]+t[v])
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    print(dp[int(input())])