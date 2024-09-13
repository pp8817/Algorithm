import sys
input = lambda: sys.stdin.readline().rstrip()

N, B = map(int, input().split())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))


def mul(U,V):
    global N
    z = [[0]*N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            x = 0
            for i in range(N):
                x += U[row][i]*V[i][col]
            z[row][col] = x%1000
    return z

def square(y, B):
    global N
    if B == 1:
        for row in range(N):
            for col in range(N):
                y[row][col] %= 1000
        return y
    
    tmp = square(y, B//2) # ex) B=4라면 tmp = matrix^2

    if B % 2 == 0: # B가 짝수라면 m*m
        return mul(tmp, tmp)
    else: # B가 홀수라면 m-1(짝수)*m
        return mul(mul(tmp, tmp), y) 
    
for i in square(matrix, B):
    print(*i)