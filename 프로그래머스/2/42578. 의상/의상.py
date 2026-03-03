def solution(clothes):
    cnt = {}
    for name, category in clothes:
        cnt[category] = cnt.get(category, 0) + 1
    
    answer = 1
    for k in cnt.values():
        answer *= (k + 1)

    return answer - 1