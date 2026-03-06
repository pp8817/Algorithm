def solution(tickets):
    dict = {}
    for s, e in tickets:
        if s in dict:
            dict[s].append(e)
        else:
            dict[s] = [e]
    for key in dict.keys():
        dict[key].sort(reverse=True)
        
    answer = []
    path = ['ICN']
    
    while path:
        now = path[-1]
        if (now not in dict) or len(dict[now]) == 0:
            answer.append(path.pop())
        else:
            path.append(dict[now].pop())

    return answer[::-1]