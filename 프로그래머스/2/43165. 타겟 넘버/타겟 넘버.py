def solution(numbers, target):
    N = len(numbers)
    answer = 0
    def dfs(cnt, num, idx):
        nonlocal answer
        if cnt == N:
            if num == target:
                answer +=1
            return
        
        dfs(cnt+1, num+numbers[idx], idx+1)
        dfs(cnt+1, num-numbers[idx], idx+1)
        
        
    dfs(0, 0, 0)
    
    return answer