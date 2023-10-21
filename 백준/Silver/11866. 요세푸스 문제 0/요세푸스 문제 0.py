import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n, k = map(int, input().split())
q = deque(range(1,n+1))
print('<', end='')
while len(q) != 0:
    for i in range(k-1):
        q.append(q.popleft())
    if len(q) == 1:
        print(f'{q.popleft()}>')
        break
    else:
        print(q.popleft(), end=', ')