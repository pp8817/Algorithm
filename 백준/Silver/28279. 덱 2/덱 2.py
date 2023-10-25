import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

de = deque()
for i in range(int(input())):
    cmd = list(map(int, input().split()))
    if cmd[0]==1:
        de.appendleft(cmd[1])
    elif cmd[0]==2:
        de.append(cmd[1])
    elif cmd[0]==3:
        if len(de) == 0:
            print(-1)
        else:
            print(de.popleft())
    elif cmd[0]==4:
        if len(de) == 0:
            print(-1)
        else:
            print(de.pop())
    elif cmd[0]==5:
        print(len(de))
    elif cmd[0]==6:
        if len(de) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0]==7:
        if len(de) == 0:
            print(-1)
        else:
            print(de[0])
    else:
        if len(de) == 0:
            print(-1)
        else:
            print(de[-1])
