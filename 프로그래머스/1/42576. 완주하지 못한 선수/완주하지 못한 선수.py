def solution(participant, completion):
    maps = {}
    for i in participant: 
        if i in maps:
            maps[i] += 1
        else:
            maps[i] = 1
    
    
    for c in completion:
        maps[c] -= 1
    
    for name, v in maps.items():
        if v:
            return name