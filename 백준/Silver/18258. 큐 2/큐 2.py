import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N = int(input())
que = deque()
for _ in range(N):
    cmd = list(input().split())

    if cmd[0] == 'push':
        que.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(que))
    elif cmd[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    else:
        if que:
            print(que[-1])
        else:
            print(-1)