
import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    q = deque(map(int, input().split()))
    nq = deque(range(N))

    cnt = 0
    while True:
        if q[0] == max(q):
            cnt += 1
            if nq[0] == M:
                print(cnt)
                break
            else: 
                q.popleft()
                nq.popleft()
        else:
            q.append(q.popleft())
            nq.append(nq.popleft())