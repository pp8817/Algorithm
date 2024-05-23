import sys
input = lambda: sys.stdin.readline().rstrip()

def back():
    if len(ans) == M:
        print(*ans)
        return
    
    overlap = 0
    for i in range(N):
        if not visited[i]:
            if overlap != m[i]:
                visited[i] = True
                ans.append(m[i])
                overlap = m[i]
                back()
                visited[i] = False
                ans.pop()

N, M = map(int, input().split())

m = sorted(list(map(int, input().split())))
ans = []
visited = [False]*N
back()