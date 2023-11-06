def solution(s, skip, index):
    abc = [chr(i) for i in range(97, 123) if not chr(i) in skip] * 3
    answer = ''
    for i in s:
        answer += abc[abc.index(i) + index]
        
    return answer