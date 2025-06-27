import sys
input = lambda: sys.stdin.readline().rstrip()

sys.setrecursionlimit(100000)

V, E = map(int, input().split())
edges = []

for _ in range(E):
    A,B,C = map(int, input().split()) # A, B 정점의 가중치 C
    edges.append((C,A,B)) # 가중치 기준으로 정렬 가능하도록

edges.sort()

parent = [i for i in range(V+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root
        return True
    return False

total_weight = 0
for cost, a, b in edges:
    if union(a,b):
        total_weight += cost

print(total_weight)