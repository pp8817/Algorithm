import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

#D 1: Q에서 최댓값 삭제, D -1: Q에서 최솟값 삭제
#I n: 정수 n을 Q에 삽입하는 연산
# Q가 비어있는데 연산 D라면 연산 무시


T = int(input())
for _ in range(T):
    min_heap = []
    max_heap = []
    k = int(input())
    check = [1] * k
    
    for i in range(k):
        command, num = input().split()
        num = int(num)

        if command == 'I':
            heapq.heappush(min_heap, (num,i))
            heapq.heappush(max_heap, (-num,i))
        else:
            if num == -1:
                if min_heap:
                    check[heapq.heappop(min_heap)[1]] = 0
            elif num == 1:
                if max_heap:
                    check[heapq.heappop(max_heap)[1]] = 0
        
        while min_heap and check[min_heap[0][1]] == 0:
            heapq.heappop(min_heap)
        while max_heap and check[max_heap[0][1]] == 0:
            heapq.heappop(max_heap)
    
    if min_heap == []:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])