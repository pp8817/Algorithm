import sys
input = lambda: sys.stdin.readline().rstrip()

def sol(m, n, x, y):
    while x <= m * n: # 최대 범위
        if (x-y) % n == 0: # 나머지로 확인
            return x
        x += m
    return -1

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(sol(M,N,x,y))