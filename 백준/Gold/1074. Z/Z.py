import sys
sys.setrecursionlimit(10**3)
input = lambda: sys.stdin.readline().rstrip()

N, r, c = map(int,input().split())
size = 2**N

def dfs(row, col, n, value):
    n = n // 2

    if row < n and col < n: # 1사분면
        if n == 1:
            print(value)
            exit(0)
        dfs(row, col, n, value) # 2**n*0

    elif row < n and col >= n: # 2사분면
        if n == 1:
            print(value + 1)
            exit(0)
        dfs(row, col - n, n, value + n ** 2 * 1) # 2**n*1

    elif row >= n and col < n: # 3사분면
        if n == 1:
            print(value + 2)
            exit(0)
        dfs(row - n, col, n, value + n ** 2 * 2) # 2**n*2

    elif row >= n and col >= n: # 4사분면
        if n == 1:
            print(value + 3)
            exit(0)
        dfs(row - n, col - n, n, value + n ** 2 * 3) # 2**n*3

dfs(r,c,size,0)
