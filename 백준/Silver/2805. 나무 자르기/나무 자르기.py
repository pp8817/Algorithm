import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
hei = list(map(int, input().split()))

start, end = 1, max(hei)

while start <= end:
    mid = (start+end)//2
    height = 0
    
    for h in hei:
        if h>mid:
            height += h-mid

    if height >= M:
        start = mid+1
    else:
        end = mid -1

print(end)