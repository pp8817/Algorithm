import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
maps = list(input())

flag = 0
ans = 0
for ch in maps:
    # 무한 루프 생성 조건
    if ch == "W" and flag:
        ans += 1
        flag = 0
    elif ch == "E":
        flag = 1

print(ans)