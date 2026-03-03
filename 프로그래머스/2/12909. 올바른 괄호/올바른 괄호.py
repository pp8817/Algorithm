from collections import deque

def solution(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append('(')
        else:
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                return False
    
    if len(stack) == 0:
        return True
    
    return False