def solution(A,B):
    answer = 0
    A.sort(); B.sort()
    
    for i in range(1, len(A)+1):
        answer += (A[i-1]*B[-i])

    return answer