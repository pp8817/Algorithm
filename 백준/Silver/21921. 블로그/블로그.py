import sys
input = lambda: sys.stdin.readline().rstrip()

N, X = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(1, N):
    arr[i] += arr[i-1]
ans = 1
max = arr[X-1]

for i in range(X, N):
    if (arr[i] - arr[i-X]) > max:
        max = arr[i] - arr[i-X]
        ans = 1
    elif (arr[i]-arr[i-X]) == max:
        ans += 1

if max == 0:
    print("SAD")
else:
    print(max)
    print(ans)