import sys
input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)

def bf():
    for i in range(N):
        for j in range(2*M+W):
            curNode, nextNode, cost = edges[j]
            
            if distance[nextNode] > distance[curNode] + cost:
                distance[nextNode] = distance[curNode] + cost
                if i == N-1: # N번째 반복에서 갱신되는 값이 있다면 Negative Cycle 존재
                    return True
    return False


TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split()) # 지점, 도로, 웜홀 개수
    edges = []
    distance = [INF]*(N+1)
    for _ in range(M):      
        S,E,T = map(int, input().split()) # 지점1, 지점2, 걸리는 시간
        edges.append((S,E,T))
        edges.append((E,S,T))
    for _ in range(W):
        S,E,T = map(int, input().split()) # 시작, 도착, 줄어드는 시간
        edges.append((S,E,-T))

    if bf():
        print("YES")
    else:
        print("NO")
    