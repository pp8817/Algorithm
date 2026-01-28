def solution(numbers, target):
    def dfs(idx, current_sum):
        
        if idx == len(numbers):
            if current_sum == target:
                return 1
            return 0
        
        return(
            dfs(idx+1, current_sum + numbers[idx])+
            dfs(idx+1, current_sum - numbers[idx])
        )
    return dfs(0, 0)
    
        