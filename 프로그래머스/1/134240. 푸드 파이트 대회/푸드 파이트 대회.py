def solution(food):
    answer=''
    food = food[1:]
    for i, c in enumerate(food):
        answer+=str(i+1)*(c//2)
    answer = answer+'0'+answer[::-1]
    return answer