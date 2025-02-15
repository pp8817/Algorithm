def solution(n, lost, reserve):
    # 여벌 체육복을 가져왔지만 도난당한 학생 제외
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    for r in sorted(reserve_set):
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)
    
    return n - len(lost_set)