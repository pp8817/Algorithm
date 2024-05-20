import sys
input = lambda: sys.stdin.readline().rstrip()

def sol(a,b,c):
    if b == 1:
        return a%c
    elif b%2==0:
        return (sol(a,b//2,c)**2)%c
    else:
        return ((sol(a,b//2,c)**2)*a)%c


A, B, C = map(int, input().split())
print(sol(A,B, C))