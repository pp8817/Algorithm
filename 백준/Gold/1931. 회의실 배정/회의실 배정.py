import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x: (x[1], x[0]))
tmp = 0 # 현재 마지막 회의 종료 시간
ans = 0

for s, t in arr:
    if s >= tmp:
        ans += 1
        tmp = t

print(ans)