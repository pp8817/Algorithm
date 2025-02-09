def solution(progresses, speeds):
    answer = []
    idx = 0
    l = len(progresses)
    
    while idx < l:
        for i in range(l):
            progresses[i] += speeds[i]
            
        temp = 0
        while idx < l and progresses[idx] >= 100:
            idx += 1
            temp += 1
            
        if temp > 0:
            answer.append(temp)
    
    return answer