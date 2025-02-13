def solution(participant, completion):
    answer = ''
    maps = {}
    
    for p in participant:
        if p in maps:
            maps[p] += 1
        else:
            maps[p] = 1
    
    for c in completion:
        maps[c] -= 1

    for key, value in maps.items():
        if value != 0:
            return key