import itertools

def solution(k, dungeons):
    answer = 0
    
    arr = list(itertools.permutations(dungeons, len(dungeons)))
    
    for i in arr:
        kk = k
        result = 0
        for j in i:
            if kk < j[0]:
                continue
            elif kk >= j[0]:
                kk -= j[1]
                result += 1
        answer = max(result, answer)       
    
    return answer        
    
