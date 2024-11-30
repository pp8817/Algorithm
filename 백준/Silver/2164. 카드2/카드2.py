import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N = int(input())
que = deque(i for i in range(1, N+1))

while len(que) >= 2:
    que.popleft()
    que.append(que.popleft())

print(que[0])