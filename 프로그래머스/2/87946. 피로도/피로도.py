def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    answer = 0
    def dfs(health, cnt):
        nonlocal answer
        if cnt > answer:
            answer = cnt
        
        for i in range(n):
            if visited[i]:
                continue
            need, minus = dungeons[i]
            if health >= need:
                visited[i] = True
                dfs(health-minus, cnt + 1)
                visited[i] = False
    
    dfs(k, 0)
    return answer
                