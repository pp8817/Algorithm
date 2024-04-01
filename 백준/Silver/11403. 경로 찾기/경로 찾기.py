import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

def dfs(x):
    for i in range(N):
        if grid[x][i] ==1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

visited = [0]*N
for i in range(N):
    dfs(i)
    for j in range(N):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visited = [0]*N