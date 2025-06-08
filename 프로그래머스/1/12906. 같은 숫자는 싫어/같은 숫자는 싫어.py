def solution(arr):
    answer = []
    temp = -1
    for num in arr:
        if temp != num:
            answer.append(num)
            temp = num
    
    return answer