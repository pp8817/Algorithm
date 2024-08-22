def solution(bandage, health, attacks):
    answer = health
    
    x,y,z = bandage # 시전 시간, 1초당 회복량, 추가 회복량
    count = 0
    time = attacks[-1][0]
    
    dict = {x[0]:x[1] for x in attacks}
    
    for i in range(1, time+1):
        count += 1
        
        if i in dict: # 현재 시간에 해당하는 공격이 있디면
            answer -= dict[i] # 데미지 만큼 체력 하락
            count = 0
            continue
        
        if answer <= 0: # 체력이 0 이하라면 -1
            return -1
        
        
        if answer < health:
            answer = min(health, answer+y)
            
            if count == x: # 시전 시간만큼 시간이 지났다면
                answer = min(health, answer+z)
                count = 0
    if answer <= 0:
        answer = -1
    return answer