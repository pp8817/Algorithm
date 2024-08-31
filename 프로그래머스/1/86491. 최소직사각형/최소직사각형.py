def solution(sizes):
    answer = 0
    w,h = [], []
    for s in sizes:
        s.sort()
        w.append(s[0])
        h.append(s[1])
        
    answer = max(w)*max(h)
    
    return answer