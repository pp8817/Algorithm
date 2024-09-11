import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

str = list(input())
boom = list(input())
m = len(boom)

stack = []

for s in str:
    stack.append(s)
    if stack[len(stack)-m:len(stack)] == boom:
        for _ in range(m):
            stack.pop()

if stack:
    print(*stack, sep="")
else:
    print("FRULA")