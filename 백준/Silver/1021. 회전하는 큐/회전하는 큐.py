import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())
que = deque(i for i in range(1,N+1))
arr = list(map(int, input().split()))

ans = 0
for i in arr:
    while True:
        if que[0] == i:
            que.popleft()
            break
        else:
            if que.index(i) < len(que)/2:
                while que[0] != i:
                    que.append(que.popleft())
                    ans += 1
            else:
                while que[0] != i:
                    que.appendleft(que.pop())
                    ans += 1
print(ans)