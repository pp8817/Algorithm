import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    entry_map = {}  # 삽입된 원소의 상태를 관리
    
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        
        if op == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            
            if num in entry_map:
                entry_map[num] += 1
            else:
                entry_map[num] = 1
        else:
            if num == 1: # 최댓값 삭제
                while max_heap and entry_map[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    value = -heapq.heappop(max_heap)
                    entry_map[value] -= 1
            else: # 최솟값 삭제
                while min_heap and entry_map[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    value = heapq.heappop(min_heap)
                    entry_map[value] -= 1
                    
    while max_heap and entry_map[-max_heap[0]] == 0:
            heapq.heappop(max_heap)
            
    while min_heap and entry_map[min_heap[0]] == 0:
            heapq.heappop(min_heap)
            
    if not max_heap or not min_heap:
        return [0,0]
    else:
        return [-max_heap[0], min_heap[0]]
