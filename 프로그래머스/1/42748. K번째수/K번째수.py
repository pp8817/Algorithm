def solution(array, commands):
    answer = []
    for i,j,k in commands:
        ar = array[i-1:j]
        ar.sort()
        answer.append(ar[k-1])
        
    return answer