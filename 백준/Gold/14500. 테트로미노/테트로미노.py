import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
d = [[1,0], [-1,0], [0,1], [0,-1]]
etc_arr = [[[-1,0],[1,0],[0,1]], [[-1,0],[1,0],[0,-1]], [[0,1],[0,-1],[1,0]], [[0,1],[0,-1],[-1,0]]]

# 최댓값 변수
maxValue = 0

def dfs(i, j, value, cnt):
    global maxValue
    
    if cnt == 4:
        maxValue = max(value, maxValue)
        return
    for dx, dy in d:
        nx, ny = i+dx, j+dy
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, value+grid[nx][ny], cnt+1)
            visited[nx][ny] = False
def etc(i, j):
    global maxValue

    for li in etc_arr:
        # 초기값
        tmp = grid[i][j]
        for dx, dy in li:
            nx, ny = i+dx, j+dy

            if not (0<=nx<N and 0<=ny<M):
                tmp = 0
                break
            tmp += grid[nx][ny]
        maxValue = max(maxValue, tmp)


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, grid[i][j], 1)
        visited[i][j] = False

        etc(i,j)
print(maxValue)