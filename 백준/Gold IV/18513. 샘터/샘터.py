import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
s = map(int, input().split())
d = [-1,1]
q = deque()
visited=set()

for i in s:
    q.append((i, 1))
    visited.add(i)
    
result = 0
build = 0
def bfs():
    global result, build
    while q:
        n, b = q.popleft()
        for dx in d:
            nx = n+dx
            if nx not in visited:
                visited.add(nx)
                result += b
                build += 1
                q.append((nx, b+1))
                if build == K:
                    return
bfs()
print(result)