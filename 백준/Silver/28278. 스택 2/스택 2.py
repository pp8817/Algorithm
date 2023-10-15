import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
stack = []

def stack_cmd(cmd):
    if cmd == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd == 3:
        print(len(stack))
    elif cmd == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif cmd == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)
    
            
for _ in range(n):
    cmd = list(map(int, input().split()))
    if len(cmd) == 1:
        stack_cmd(cmd[0])
    else:
        x = int(cmd[1])
        stack.append(x)