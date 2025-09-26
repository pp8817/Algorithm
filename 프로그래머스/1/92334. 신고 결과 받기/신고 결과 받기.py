def solution(id_list, report, k):
    report = set(report)
    report_count = {id:0 for id in id_list} # 신고 당한 내역
    id_to_index = {id:index for index, id in enumerate(id_list)} #신고자 내역
        
    for ch in report:
        a, b = ch.split(" ")
        report_count[b] += 1
    
    answer = [0]*len(id_list)
    for ch in report:
        a, b = ch.split(" ")
        if report_count[b] >= k:
            answer[id_to_index[a]] += 1
        
    return answer