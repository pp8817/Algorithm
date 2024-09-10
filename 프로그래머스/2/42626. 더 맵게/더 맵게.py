import heapq

def solution(scoville, K): # 스코빌 지수 배열, 목표 스코빌
    answer = 0
    arr = []
    for i in scoville:
        heapq.heappush(arr, i)
    
    while len(arr) > 1:
        a = heapq.heappop(arr)
        if a >= K:
            break
        b = heapq.heappop(arr)
        
        heapq.heappush(arr, a + b*2)
        answer += 1
    
    if len(arr) == 0:
        return -1
    elif len(arr) == 1:
        if arr[0] < K:
            return -1
        
    return answer
        
    