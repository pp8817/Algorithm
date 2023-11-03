def solution(keymap, targets):
    dic = {}
    for k in keymap:
        for i, w in enumerate(k):
            if (w in dic) and (i + 1) > dic[w]:
                continue
            dic[w] = i + 1 
    answer = []
    for target in targets:
        total = 0
        
        for alp in target:
            if alp in dic:
                total += dic[alp]
            else:
                total = -1
                break
        answer.append(total)
    return answer
