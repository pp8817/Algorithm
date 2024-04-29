import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
                
N, M = map(int, input().split())

lop = {}

for i in range(N+M):
    x, y = map(int, input().split())
    lop[x]=y


q = deque([1])
visited = [0]*101
l = lop.keys()
    
while q:
    v = q.popleft()

    if v==100:
        print(visited[100])
        break
        
    for i in range(1, 7):
        nv = v+i
        if nv<101 and not visited[nv]:
            if nv in l:
                nv = lop[nv]
            if not visited[nv]:
                visited[nv] = visited[v] + 1
                q.append(nv)