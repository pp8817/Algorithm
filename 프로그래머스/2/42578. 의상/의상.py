def solution(clothes):
    answer = 1
    
    maps = {i[1]:1 for i in clothes}
    for clothe, category in clothes:
        maps[category] += 1
    
    for i in maps.values():
        answer *= i
    return answer-1