import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = []
total_num = 0
for _ in range(N):
    idx, num = map(int, input().split())
    arr.append((idx, num))
    total_num += num

total_num /= 2

arr.sort(key=lambda x: x[0])

tmp = 0
for i in range(N):
    idx, num = arr[i]
    tmp += num

    if tmp >= total_num:
        print(idx)
        break