import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, g = map(int, input().split())
    tree[a].append((b,g))
    tree[b].append((a,g))
    
def dfs(node, s):
    for n, w in tree[node]:
        sw = s + w
        if visited[n] == -1:
            visited[n] = sw
            dfs(n, sw)
    return

visited = [-1]*(n+1)
visited[1] = 0
dfs(1,0)

idx, tmp = 0,0

for i in range(1, len(visited)):
    if visited[i] > tmp:
        tmp = visited[i]
        idx = i

visited = [-1]*(n+1)
visited[idx] = 0
dfs(idx, 0)

print(max(visited))