def solution(routes):
    answer = 0
    routes.sort(key = lambda x: x[1])
    camera = -30001
    
    for start, end in routes:
        if start > camera:
            answer += 1
            camera = end
    
    return answer