def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve) # 여벌 체육복을 자신이 사용하는 경우 제외
    set_reserve = set(reserve) - set(lost) # 여벌 체육복을 자신이 사용하는 경우 제외

    for r in sorted(set_reserve):
        if r-1 in set_lost:
            set_lost.remove(r-1)
        elif r+1 in set_lost:
            set_lost.remove(r+1)
    return n-len(set_lost)
            