def solution(progresses, speeds):
    days = []
    for p, s in zip(progresses, speeds):
        days.append(((100-p)+s-1)//s)
    
    cnt = 1
    answer = []
    current = days[0]
    
    for d in days[1:]:
        if current >= d:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            current = d
    answer.append(cnt)
    return answer
    
        