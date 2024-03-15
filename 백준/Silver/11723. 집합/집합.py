import sys
input = lambda: sys.stdin.readline().rstrip()

stack = []
def calculator(s, n):
    global stack
    
    if s == "add":
        if n not in stack:
            stack.append(n)
    elif s == "remove":
        if n in stack:
            del stack[stack.index(n)]

    elif s == "check":
        if n in stack:
            print(1)
        else:
            print(0)

    elif s == "toggle":
        if n in stack:
            del stack[stack.index(n)]
        else:
            stack.append(n)
def calculator2(s):
    global stack
    if s == "all":
        stack = [i for i in range(1,21)]
    
    elif s == "empty":
        stack.clear()

M = int(input())
for _ in range(M):
    li = list(input().split())
    if len(li) == 1:
        calculator2(li[0]) 
    else:
        calculator(li[0], int(li[1]))