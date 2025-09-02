from collections import Counter

def solution(topping):
    answer = 0
    right = Counter(topping) # 총 토핑 갯수
    rightKinds = len(right)
    
    left = set()
    
    for i in range(len(topping)-1):
        t = topping[i]
        left.add(t)
        
        right[t] -= 1
        if right[t] == 0:
            rightKinds -= 1
            del right[t]
        
        if len(left) == rightKinds:
            answer += 1
        
    return answer