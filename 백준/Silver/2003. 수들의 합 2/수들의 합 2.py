import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
temp = 0
ans = 0

while True:
    if temp >= M:
        temp -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        temp += arr[right]
        right += 1

    if temp == M:
        ans += 1

print(ans)