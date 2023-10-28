import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n = int(input())
q = deque(enumerate(map(int, input().split())))
res = []

while q:
    idx, paper = q.popleft()
    res.append(idx + 1)

    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)

print(*res)