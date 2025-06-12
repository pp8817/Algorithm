def solution(number):
    answer = 0
    N = len(number)
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if number[i]+number[j]+number[k] == 0:
                    answer += 1
        
    return answer
