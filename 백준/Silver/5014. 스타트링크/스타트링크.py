import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

F, S, G, U, D = map(int, input().split())

visited = [0] * (F + 1)
q = deque()
q.append(S)
visited[S] = 1  # 시작 지점은 방문 표시만, 나중에 -1 해줄 것

while q:
    now = q.popleft()

    if now == G:
        print(visited[now] - 1)
        break

    # 위로 이동
    if U > 0:
        next_up = now + U
        if next_up <= F and visited[next_up] == 0:
            visited[next_up] = visited[now] + 1
            q.append(next_up)

    # 아래로 이동
    if D > 0:
        next_down = now - D
        if next_down >= 1 and visited[next_down] == 0:
            visited[next_down] = visited[now] + 1
            q.append(next_down)
else:
    print("use the stairs")