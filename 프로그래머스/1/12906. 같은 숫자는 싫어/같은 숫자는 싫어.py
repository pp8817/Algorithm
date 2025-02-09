def solution(arr):
    answer = []
    temp = -1
    for a in arr:
        if temp != a:
            answer.append(a)
            temp = a
    
    return answer