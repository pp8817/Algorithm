def solution(cookie):
    n = len(cookie)
    answer = 0
    
    for m in range(n-1):
        l = m
        r = m+1
        
        left_sum = cookie[l]
        right_sum = cookie[r]
        
        while True:
            if left_sum == right_sum:
                answer = max(answer, left_sum)
                
                # 양 쪽 모두 확장
                l -= 1
                r += 1
                if l < 0 or r >= n:
                    break
                left_sum += cookie[l]
                right_sum += cookie[r]
            
            elif left_sum < right_sum:
                # 왼쪽 확장
                l -= 1
                if l < 0:
                    break
                left_sum += cookie[l]
            else:
                # 오른쪽 확장
                r += 1
                if r >= n:
                    break
                right_sum += cookie[r]
                
    return answer