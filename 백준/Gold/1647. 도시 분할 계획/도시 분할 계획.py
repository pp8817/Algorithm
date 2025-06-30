import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C,A,B))

edges.sort()

parent = [i for i in range(N+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        parent[b_root] = a_root
        return True
    return False

mst_count = 0
max_edge = 0

for cost, a, b in edges:
    if union(a, b):
        mst_count += cost
        max_edge = max(max_edge, cost)

print(mst_count - max_edge)