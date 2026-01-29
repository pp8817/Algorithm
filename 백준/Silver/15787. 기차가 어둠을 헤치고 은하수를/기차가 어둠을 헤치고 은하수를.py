import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())
train = [[0]*20 for _ in range(N+1)]

for _ in range(M):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        i, x = cmd[1], cmd[2]
        train[i][x-1] = 1
    elif cmd[0] == 2:
        i, x = cmd[1], cmd[2]
        train[i][x-1] = 0
    elif cmd[0] == 3:
        i = cmd[1]
        train[i] = [0] + train[i][:19]
    else:
        i = cmd[1]
        train[i] = train[i][1:] + [0]

seen = set()
for i in range(1, N+1):
    seen.add(tuple(train[i]))

print(len(seen))