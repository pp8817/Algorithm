import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = N-1

ans = abs(arr[start] + arr[end])
result = [arr[start], arr[end]]

while start < end:
    s = arr[start] + arr[end]

    if abs(s) < ans:
        ans = abs(s)
        result = [arr[start], arr[end]]
        if ans == 0:
            break

    if s < 0:
        start += 1
    else:
        end -= 1

print(result[0], result[1])