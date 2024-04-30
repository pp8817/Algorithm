import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def bfs(A, B):
    q = deque()
    q.append([A, ''])
    visited = [False]*10001
    visited[A]=True

    while q:
        a, command = q.popleft()
        
        if a == B:
            return command
        
        d = a * 2 % 10000
        if not visited[d]:
            visited[d] = True
            q.append([d, command + 'D'])

        s = (a - 1) % 10000
        if not visited[s]:
            visited[s] = True
            q.append([s, command + 'S'])

        l = a // 1000 + (a % 1000)*10
        if not visited[l]:
            visited[l] = True
            q.append([l, command + 'L'])

        r = a // 10 + (a % 10) * 1000
        if not visited[r]:
            visited[r] = True
            q.append([r, command + 'R'])


T = int(input())
for _ in range(T):
    A, B = map(int, input().split()) # 10000>A, B>=0
    print(bfs(A, B))