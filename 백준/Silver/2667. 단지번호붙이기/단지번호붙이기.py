import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(r,c):
    global count
    if promissing(r,c):
        count += 1
        visited[r][c] = True
        for dx, dy in d:
            dfs(r+dx, c+dy)   

def promissing(r,c):
    if 0<=r<N and 0<=c<N and graph[r][c] == 1 and not visited[r][c]:
        return True
    else:
        return False

N = int(input())
graph = [[] for _ in range(N)]

for i in range(N):
    row = input()
    for r in row:
        graph[i].append(int(r))

visited = [[False]*N for _ in range(N)]
d = [[1,0], [-1,0], [0,1], [0,-1]]
count = 0
count_list = []
ans = 0

for i in range(N):
    for j in range(N):
        if promissing(i,j):
            dfs(i,j)
            count_list.append(count)
            count = 0
            ans += 1

count_list.sort()
print(ans)
for c in count_list:
    print(c)