from collections import deque

def solution(priorities, location):
    q = deque(priorities)
    answer = 0
    
    while q:
        p = q.popleft()
        
        if len(q) == 0:
            answer += 1
            break
            
        if p < max(q):
            q.append(p)

        else:
            answer += 1
            if location == 0:
                break
                
        location -= 1
        if location < 0:
            location = len(q)-1
    
    return answer