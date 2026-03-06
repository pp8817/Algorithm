def solution(people, limit):
    people.sort()
    answer = 0
    
    l, r = 0, len(people)-1
    while l<r:
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
        else:
            r -= 1
        answer += 1
    
    if l == r:
        answer += 1
    
    return answer