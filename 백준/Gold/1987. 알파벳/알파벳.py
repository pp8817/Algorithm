import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(r, c, count):
    global ans
    ans = max(ans, count)
    for x, y in d:
        rr,cc = r+x, c+y
        if 0 <= rr < R and 0 <= cc < C and maps[rr][cc] not in alphas:
            alphas.add(maps[rr][cc])
            dfs(rr,cc, count+1)
            alphas.remove(maps[rr][cc])

R, C = map(int, input().split())

maps = [list(input()) for _ in range(R)]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

alphas = set(maps[0][0])
ans = 0
dfs(0,0,1)
print(ans)