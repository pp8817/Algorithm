def solution(number, k):
    stack = []
    for num in number:
        while len(stack) != 0 and num > stack[-1] and k != 0:
            stack.pop()
            k -=1
        stack.append(num)
    
    if k > 0:
        return "".join(stack[:-k])
    
    return "".join(stack)