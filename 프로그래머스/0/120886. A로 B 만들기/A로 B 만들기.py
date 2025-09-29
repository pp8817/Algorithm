def solution(before, after):
    maps = {}

    for ch in after:
        maps[ch] = maps.get(ch, 0) + 1

    for ch in before:
        if ch not in maps:
            return 0
        maps[ch] -= 1
        if maps[ch] < 0:
            return 0
    
    return 1