import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))

for i in range(1,n):
    arr[i] = max(arr[i], arr[i] + arr[i-1])

print(max(arr))