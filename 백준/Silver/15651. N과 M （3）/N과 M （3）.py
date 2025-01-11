import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs():
    if len(s) == M:
        print(" ".join(map(str, s)))
        return
    
    for i in range(1, N+1):
        s.append(i)
        dfs()
        s.pop()

N, M = map(int, input().split())
s = []

dfs()