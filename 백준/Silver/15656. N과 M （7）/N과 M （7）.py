import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
tmp = []

def dfs():
    if len(tmp) == M:
        print(*tmp)
        return
    
    for i in range(N):
        tmp.append(arr[i])
        dfs()
        tmp.pop()

dfs()