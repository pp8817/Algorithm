import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [False]*N
ans = int(1e9)

def dfs(L, idx):
    global ans
    if N//2 == L:
        A, B = 0,0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += S[i][j]
                elif not visited[i] and not visited[j]:
                    B += S[j][i]
        ans = min(ans, abs(A-B))
        return

    for i in range(idx, N):
        visited[i] = True
        dfs(L+1, i+1)
        visited[i] = False

dfs(0,0)
print(ans)