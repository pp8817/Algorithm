import sys
input = lambda: sys.stdin.readline().rstrip()

A, B, C = map(int, input().split())

def sol(x, n):
    if n == 1:
        return A%C
    else:
        tmp = sol(x, n//2)
        if n%2==0:
            return (tmp*tmp)%C
        else:
            return (tmp*tmp*A)%C

print(sol(A,B))