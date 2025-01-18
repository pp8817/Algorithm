import sys
input = lambda: sys.stdin.readline().rstrip()

# 가장 큰 정사각형의 넓이 출력
# 1: 채워진 부분, 0: 안채워진 부분
n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, list(input()))))

res = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and i > 0 and j > 0:
            arr[i][j] += min(arr[i][j-1], arr[i-1][j], arr[i-1][j-1])
        res = max(res, arr[i][j])
print(res*res)