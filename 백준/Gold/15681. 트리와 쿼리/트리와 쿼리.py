import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

N, R ,Q = map(int, input().split()) # 정점의 수, 루트 번호, 쿼리 수
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    U,V = map(int, input().split()) # U,V를 양 끝점으로 하는 간선
    graph[U].append(V)
    graph[V].append(U)


subtree_size = [0]*(N+1)
def dfs(node, parent):
    subtree_size[node] = 1
    
    for child in graph[node]:
        if child != parent:
            dfs(child, node)
            subtree_size[node] += subtree_size[child]
dfs(R, -1)

for _ in range(Q):
    # 정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력한다.
    print(subtree_size[int(input())])