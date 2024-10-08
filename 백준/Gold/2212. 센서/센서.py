import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input()) # 센서 개수
K = int(input()) # 집중국 개수
arr = list(map(int, input().split())) # 센서의 좌표

if N <=K:
    print(0)
else:
    arr.sort()


    m = []
    for i in range(1, N):
        m.append(arr[i] - arr[i-1])
    m.sort()

    for _ in range(K-1):
        m.pop()
    print(sum(m))