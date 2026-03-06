def solution(n, computers):
    def dfs(row, computers):
        for i in range(n):
            if computers[row][i] == 1:
                computers[row][i] = 0
                computers[i][row] = 0
                dfs(i, computers)
    
    answer = 0
    for i in range(n):
        if computers[i][i] == 1:
            dfs(i, computers)
            answer += 1
    
    return answer