import sys
input = lambda: sys.stdin.readline().rstrip()

def binary_search(v, dir):
    left, right = 0, N-1

    while left <= right:
        mid = (left+right)//2

        if v < arr[mid]:
            right = mid - 1
        elif v > arr[mid]:
            left = mid+1
        else:
            return mid
        
    if dir == 0:
        return left
    else:
        return right

N, M = map(int, input().split()) # 점의 개수, 선분의 개수
arr = sorted(list(map(int, input().split()))) # 점의 좌표


for i in range(M):
    s, e = map(int, input().split())
    l, r = binary_search(s, 0), binary_search(e, 1)
    print(r-l+1)