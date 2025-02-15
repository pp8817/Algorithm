def solution(citations):
    h_index = 0
    citations.sort(reverse=True)
    N = len(citations)
    
    for i in range(N):
        if citations[i] < i+1:
            return i
        
    return N