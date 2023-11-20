def solution(food):
    answer=''
    food = food[1:]
    for i, c in enumerate(food):
        c = c//2
        
        if c>=1:
            answer+=str(i+1)*c
    answer = answer+'0'+answer[::-1]
    return answer