from collections import deque
def solution(cards1, cards2, goal):
    c1 = deque(cards1)
    c2 = deque(cards2)
    
    for w in goal:
        if (len(c1) != 0) and (w == c1[0]):
            c1.popleft()
        elif (len(c2) != 0) and w == c2[0]:
            c2.popleft()
        else:
            return "No"
    return "Yes"