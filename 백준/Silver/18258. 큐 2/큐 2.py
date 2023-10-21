import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

q = deque()
for i in range(int(input())):
    co = list(input().split())
    com = co[0]
    
    if com == 'push':
        q.append(int(co[1]))
    elif com == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif com == 'size':
        print(len(q))
    elif com == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif com == 'front':
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    else:
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])