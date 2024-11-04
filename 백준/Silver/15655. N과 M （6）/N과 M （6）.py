import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
tmp = []

def dfs(start):
    if len(tmp) == M:
        print(*tmp)
        return
    
    for i in range(start, N):
        tmp.append(arr[i])
        dfs(i+1)
        tmp.pop()

dfs(0)