import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(N):
        if arr[i] not in s:
            s.append(arr[i])
            dfs()
            s.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []
dfs()