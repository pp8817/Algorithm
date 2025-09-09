def solution(order):
    n = len(order)
    stack = []
    idx = 1      
    temp = 0     
    answer = 0

    while True:
        if idx <= n and idx == order[temp]:
            # 벨트 -> 트럭
            answer += 1
            temp += 1
            idx += 1
        elif stack and stack[-1] == order[temp]:
            # 보조 컨테이너 -> 트럭
            stack.pop()
            answer += 1
            temp += 1
        elif idx <= n:
            # 벨트 -> 보조 컨테이너
            stack.append(idx)
            idx += 1
        else:
            break

    return answer