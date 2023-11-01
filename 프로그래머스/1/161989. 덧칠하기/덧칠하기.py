def solution(n, m, section):
    dic = {i:1 for i in range(1, n+1)}
    for i in section:
        dic[i] = 0
    answer = 0
    i = 1
    while n>=i:
        if dic[i] == 0:
            answer += 1
            i += m
        else:
            i+=1
    return answer