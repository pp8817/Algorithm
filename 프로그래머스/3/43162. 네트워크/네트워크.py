def solution(n, computers):
    def dfs(row, computers):
        for adj in range(n):
            if computers[row][adj] == 1:
                computers[row][adj] = 0 
                computers[adj][row] = 0 
                dfs(adj, computers)
    
    answer = 0
    for i in range(n):
        if computers[i][i] == 1:
            dfs(i, computers)   
            answer += 1 
    return answer

