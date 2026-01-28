def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        temp = 0
        flag = 1
        
        for ch in tree:
            if ch not in skill:
                continue
            if ch == skill[temp]:
                temp += 1
            else:
                flag = 0
                break
        
        if flag:
            answer += 1
        
    return answer