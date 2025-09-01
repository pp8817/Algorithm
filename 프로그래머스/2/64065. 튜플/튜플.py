def solution(s):
    answer = []
    parts = s[2:-2].split("},{")

    sets = [set(map(int, part.split(','))) for part in parts]
    sets.sort(key=len)
    
    for s in sets:
        for num in s:
            if num in answer:
                continue
            answer.append(num)
    
    return answer