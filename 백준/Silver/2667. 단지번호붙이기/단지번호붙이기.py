import sys
input = sys.stdin.readline

def dfs(x, y):
    if is_promissing(x, y):
        visited[x][y] = 1
        for nx, ny in d:
            dfs(x + nx, y + ny)

def is_promissing(row, col):
    if 0 <= row < N and 0 <= col < N and grid[row][col] == 1 and visited[row][col] == 0:
        global count
        count+=1
        return True
    else:
        return False

N = int(input())
grid = [[] for _ in range(N)]
visited = [[0] * N for _ in range(N)]

for i in range(N):
    row = input()
    for j in range(N):
        grid[i].append(int(row[j]))

d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
count = 0
result=0
c = []
for i in range(N):
    for j in range(N):
        if is_promissing(i, j):
            dfs(i, j)
            result+=1
            c.append(count-1)
            count=0
print(result)
c.sort()
for i in c:
    print(i)