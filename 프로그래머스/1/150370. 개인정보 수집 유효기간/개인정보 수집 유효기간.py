def solution(today, terms, privacies): # 오늘 날짜, 약관 유효기간, 개인정보
    answer = []
    term_dict = {}
    
    ty, tm, td = map(int, today.split("."))
    
    # 약관 유효기간을 딕셔너리에 저장
    for term in terms:
        term_name, term_duration = term.split()
        term_dict[term_name] = int(term_duration)
        
    # 개인정보마다 유효기간 확인
    for i, privacy in enumerate(privacies):
        date, term_type = privacy.split()
        y, m, d = map(int, date.split("."))
        duration = term_dict[term_type]
    
        # 유효기간 더하기
        m += duration
        y += (m - 1) // 12
        m = (m - 1) % 12 + 1
        
        # 파기해야 하는지 확인
        if y < ty or (y == ty and m < tm) or (y == ty and m == tm and d <= td):
            answer.append(i + 1)
    
    return answer