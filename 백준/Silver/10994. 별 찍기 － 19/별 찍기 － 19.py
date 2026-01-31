import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
length = (4*N)-3

ans = [[" "]*length for _ in range(length)]

def sol(n, r, c):
    global ans
    length = (4*n)-3

    if n == 1:
        ans[r][c] = "*"
        return
    
    for i in range(length):
        ans[r][c+i] = "*"
        ans[r+i][c] = "*"
        ans[r+i][c+length-1] = "*"
        ans[r+length-1][c+i] = "*"
    
    sol(n-1, r+2, c+2)

sol(N,0,0)

for row in ans:
    print("".join(row))