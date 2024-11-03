import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
request = list(map(int, input().split()))
budget = int(input())

start, end = 1, max(request)

while start <= end:
    mid = (start+end)//2
    tmp = 0

    for b in request:
        if b > mid:
            tmp += mid
        else:
            tmp += b

    if tmp <= budget:
        start = mid + 1
    else:
        end = mid - 1
print(end)