def solution(arr):
    m = max(arr)
    N = len(arr)
    while True:
        c = 0
        for num in arr:
            if m%num==0:
                c += 1
            else:
                break
        
        if c == N:
            return m
        
        m += 1