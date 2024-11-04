import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split()) # 입국심사대 갯수, 사람 수
T = [int(input()) for _ in range(N)]

start, end = min(T), max(T)*M
ans = end

while start <= end:
    total = 0
    mid = (start+end)//2

    for t in T:
        total += (mid//t)

    if total >= M:
        end = mid - 1
        ans = min(mid, ans)
    else:
        start = mid + 1
print(ans)