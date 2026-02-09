def solution(numbers):
    N = len(numbers)
    answer = [-1] * N
    stack = []  # 아직 뒷 큰 수를 못 찾은 index 저장
    
    for i in range(N):
        # 현재 값이 스택 top이 가리키는 값보다 크면
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]

        stack.append(i)

    return answer