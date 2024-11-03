import sys
input = lambda: sys.stdin.readline().rstrip()

K, N = map(int, input().split())
lt = [int(input()) for _ in range(K)]

start, end = 1, max(lt)

while start<=end:
    mid = (start+end)//2
    lines = 0

    for l in lt:
        lines += l//mid
    
    if lines>=N: # 기준 충족
        start = mid+1
    else:
        end = mid-1

print(end)