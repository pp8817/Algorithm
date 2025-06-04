def solution(participant, completion):
    maps = {}
    for p in participant:
        if p in maps:
            maps[p] += 1
        else:
            maps[p] = 1
    
    for c in completion:
        maps[c] -= 1
    
    for name, c in maps.items():
        if c != 0:
            return name