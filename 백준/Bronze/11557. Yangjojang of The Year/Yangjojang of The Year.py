import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    uv = ""
    sul = 0
    for _ in range(N):
        S, L = input().split()
        if int(L)>sul:
            uv = S
            sul = int(L)
    print(uv)