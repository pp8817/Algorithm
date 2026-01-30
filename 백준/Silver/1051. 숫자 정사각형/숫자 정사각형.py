import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]

ans = 1

for i in range(N):
    for j in range(M):
        num = arr[i][j]
        for k in range(j+1, M):
            if arr[i][k] == num:
                length = i+k-j
                if length < N and arr[length][j] == num and arr[length][k] == num:
                    ans = max(ans, (k-j+1)**2)

print(ans)