def solution(d, budget):
    answer = 0
    d.sort()
    
    for m in d:
        if m <= budget:
            budget -= m
            answer += 1
    return answer