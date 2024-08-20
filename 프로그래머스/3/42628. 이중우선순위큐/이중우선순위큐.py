import heapq

def solution(operations):
    pmax = []
    pmin = []
    
    count = 0
    
    for order in operations:
        a,b = map(str, order.split())
        b = int(b)
        if a == "I":
            heapq.heappush(pmin, b)
            heapq.heappush(pmax, -b)
            count += 1
        else:
            if count == 0:
                continue
            if b == 1: # 큐에서 최댓값을 삭제
                value = heapq.heappop(pmax)
                pmin.remove(-value)
                
            else: # 큐에서 최솟값을 삭제
                value = heapq.heappop(pmin)
                pmax.remove(-value)
                
            count -= 1
                
    if count == 0:
        return [0,0]
    else:
        return [max(pmin), min(pmin)]