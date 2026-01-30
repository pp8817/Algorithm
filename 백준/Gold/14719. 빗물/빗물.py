import sys
input = lambda: sys.stdin.readline().rstrip()

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

ans = 0
stack = []
max_left = 0

for block in blocks:
    if not stack:
        max_left = block
        stack.append(block)
        continue

    # 현재 블록이 왼쪽 벽보다 높거나 같으면 그동안 쌓인 물 정산
    if max_left <= block:
        while stack:
            ans += max_left - stack.pop()
        max_left = block
    
    stack.append(block)


# 남은 블록 처리
if stack:
    max_right = stack.pop()
    while stack:
        current = stack.pop()
        if max_right < current:
            max_right = current
        else:
            ans += max_right - current

print(ans)