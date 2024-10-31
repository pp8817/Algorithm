import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = [input().split() for _ in range(N)]
arr.sort(key=lambda x: int(x[1])) # 오름차순 정렬

chars = [int(input()) for _ in range(M)]

for char in chars:
    right = len(arr)
    left = 0
    result = 0

    while left <= right:
        mid = (left+right)//2
        if int(arr[mid][1]) >= char:
            result = mid
            right = mid-1
        else:
            left = mid + 1
    print(arr[result][0])