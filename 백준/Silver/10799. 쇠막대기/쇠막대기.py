import sys
input = lambda: sys.stdin.readline().rstrip()

li = list(input())

ans = 0
stack = []

for i in range(len(li)):
    if li[i] == '(':
        stack.append(li[i])
    elif li[i] == ')':
        if li[i-1] == '(': #레이저 
            stack.pop()
            ans += len(stack)
        else:
            ans += 1
            stack.pop()
print(ans)