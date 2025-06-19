def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        num = absolutes[i]
        
        if signs[i] == False:
            answer += num*(-1)
        else:
            answer += num
            
    return answer