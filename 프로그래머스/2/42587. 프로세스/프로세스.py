from collections import deque

def solution(priorities, location):
    q = deque()
    for i in range(len(priorities)):
        q.append((i, priorities[i]))
        
    M = max(priorities)
    cnt = 1
    while q:
        idx, temp = q.popleft()
        
        if temp == M:
            if idx == location:
                return cnt
            if len(q) > 0:
                M = max(q, key=lambda x: x[1])[1]
            cnt += 1
        else:
            q.append((idx, temp))