def solution(k, score):
    answer = []
    li = []
    for i in score:
        li.append(i)
        li.sort(reverse=True)
        
        if len(li)<k:
            answer.append(li[-1])
        else:
            answer.append(li[k-1])
    return answer