import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr1 = [list(input()) for _ in range(n)] #.: 지뢰x, *: 지뢰 o
arr2 = [list(input()) for _ in range(n)] #x: 열린칸, .: 열리지 않은 칸
result = [['.']*n for _ in range(n)]

def check(r,c):
    count = 0
    for i in range(max(0,r-1), min(r+2, n)):
        for j in range(max(0,c-1), min(c+2, n)):
            if arr1[i][j] == "*":
                count += 1

    return count

flag = False
for i in range(n):
    for j in range(n):
        if arr2[i][j] == 'x':
            if arr1[i][j] == ".":
                count = check(i,j)
                result[i][j] = str(count)
            else: # 열린칸이 폭탄이라면
                flag = True

if flag:
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '*':
                result[i][j] = '*'
    
for r in result:
    print(*r, sep="")