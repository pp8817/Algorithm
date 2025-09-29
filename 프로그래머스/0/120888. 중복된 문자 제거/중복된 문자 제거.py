def solution(my_string):
    answer = ''
    alpha = []
    for ch in my_string:
        if ch not in alpha:
            answer += ch
            alpha.append(ch)
    return answer