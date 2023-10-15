import sys
input = lambda: sys.stdin.readline().rstrip()

def check_parens(PS):
    stack = []

    for c in PS:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return "NO"
            elif "(" != stack[-1]:
                return "NO"
            else:
                stack.pop()
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"

    
T = int(input())
for _ in range(T):
    print(check_parens(input()))