def solution(s):
    answer = ''
    index = 0  # 단어 내에서의 문자 위치 (공백이 나오면 0으로 초기화)

    for ch in s:
        if ch == ' ':
            answer += ' '
            index = 0 
        else:
            if index % 2 == 0:
                answer += ch.upper()
            else:
                answer += ch.lower()
            index += 1
    
    return answer