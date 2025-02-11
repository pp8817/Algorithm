from collections import deque

def solution(s):
    answer = False
    q = deque(s)
    check = 0
    
    while q:
        x = q.popleft()
        if x == "(":
            check += 1
        else:
            check -= 1
        
        if check < 0:
            return False
        
    if check == 0:
        return True
    
    return False