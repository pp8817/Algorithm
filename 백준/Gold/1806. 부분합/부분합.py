import sys
input = lambda: sys.stdin.readline().rstrip()

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
total_sum = arr[0]
answer = int(1e9)

while right < N:
    if total_sum >= S:
        answer = min(answer, right - left + 1)
        total_sum -= arr[left]
        left += 1
    else: # total_sum < S
        right += 1
        if right < N:
            total_sum += arr[right]

if answer == int(1e9):
    print(0)
else:
    print(answer)