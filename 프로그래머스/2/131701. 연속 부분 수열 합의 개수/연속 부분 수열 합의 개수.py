def solution(elements):
    n = len(elements)
    used = set(elements) 
    used.add(sum(elements)) 

    doubled = elements + elements 

    for length in range(2, n):
        for start in range(n):
            used.add(sum(doubled[start : start + length]))

    return len(used)