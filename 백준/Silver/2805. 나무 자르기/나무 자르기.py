import sys
input = lambda: sys.stdin.readline().rstrip()


# (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)
N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)


while start<=end:
    mid = (start+end)//2

    log = 0
    for i in trees:
        if i>mid:
            log += (i-mid)
    if log >= M:
        start = mid + 1
    else:
        end = mid-1
print(end)