def solution(k, tangerine):
    maps = {}
    for t in tangerine:
        if t in maps:
            maps[t] += 1
        else:
            maps[t] = 1
    
    sorted_items = sorted(maps.items(), key=lambda x: x[1], reverse=True)
    
    ans = 0
    for _, c in sorted_items:
        ans += 1
        k -= c
        if k <= 0:
            break
    
    return ans