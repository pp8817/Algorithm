import sys
input = lambda: sys.stdin.readline().rstrip()

K = int(input())
arr = list(map(int, input().split()))
result = [[] for _ in range(K)]

def sol(l,r,k):
    if l>r:
        return

    mid = (l+r)//2
    result[k].append(arr[mid])

    sol(l, mid-1, k+1)
    sol(mid+1, r, k+1)

sol(0, len(arr)-1, 0)

for row in result:
    print(*row)