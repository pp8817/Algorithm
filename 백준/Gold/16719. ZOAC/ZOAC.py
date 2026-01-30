import sys
input = lambda: sys.stdin.readline().rstrip()

S = list(input())
n = len(S)
visited = [False] * n

def sol(l, r):
    if l > r:
        return

    idx = l
    for i in range(l, r + 1):
        if S[i] < S[idx]:
            idx = i

    visited[idx] = True
    print(''.join(S[i] for i in range(n) if visited[i]))

    sol(idx + 1, r)
    sol(l, idx - 1)

sol(0, n - 1)