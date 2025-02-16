def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    start, end = 0, len(people)-1
    
    while start <= end:
        x1, x2 = people[start], people[end]
        answer += 1
        
        if x1+x2 <= limit:
            start += 1
            end -= 1
        else:
            start += 1
        
    if not len(people):
        answer += 1
        
    return answer