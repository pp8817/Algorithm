def solution(numbers):
    answer = []
    N = len(numbers)
    
    for i in range(N):
        for j in range(i+1, N):
            num = numbers[i] + numbers[j]
            if num not in answer:
                answer.append(num)
        answer.sort()
    return answer