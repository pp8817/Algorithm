import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())

start,end = 0, n-1
ans = 0
while start < end:
    tmp = arr[start] + arr[end]
    if tmp == x:
        ans += 1
        start += 1
    elif tmp < x:
        start += 1
    else:
        end -= 1

print(ans)