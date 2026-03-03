def solution(citations):
    N = len(citations)
    citations.sort(reverse=True)
    h = 0
    for i in range(N):
        c = citations[i]
        if c >= i+1:
            h = i + 1
        else:
            break
        
    return h