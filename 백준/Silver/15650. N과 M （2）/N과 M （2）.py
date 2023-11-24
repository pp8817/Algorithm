import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs():
    if len(s) == m: # 출력 조건
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if visited[i]: #이미 방문한 숫자라면 패스
            continue
        for j in range(1,i+1):
            visited[j] = True
        s.append(i)
        dfs()
        s.pop()
        for j in range(1,i+1):
            visited[j] = False

n, m = map(int, input().split())
visited = [False] * (n+1)
s = []

dfs()