def solution(t, p):
    p_len = len(p)
    cou = 0
    for i in range(0, len(t)):
        num = t[i:i+p_len]
        if (len(num) == len(p)) and (int(p)>=int(num)) :
            cou += 1
    
    return cou