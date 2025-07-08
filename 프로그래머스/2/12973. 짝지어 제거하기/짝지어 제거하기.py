def solution(s):
    stack = []
    for i in range(len(s)):
        ch = s[i]
        if not stack:
            stack.append(ch)
        elif stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    
    if not stack:
        return 1
    else:
        return 0