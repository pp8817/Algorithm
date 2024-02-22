def solution(k, m, score):
    score = sorted(score, reverse=True)
    answer = 0
    for i in range(1, len(score)//m+1):
        answer += score[(m*i)-1]*m
    return answer
        