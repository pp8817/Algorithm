def solution(numbers, target):
    answer = [0]
    
    def dfs(index, number, value):
        value += number

        if value == target and index == len(numbers)-1:
            answer[0] += 1

        index += 1
        if index < len(numbers):
            dfs(index, numbers[index], value)
            dfs(index, numbers[index]*(-1), value)

    
    dfs(0, numbers[0], 0)
    dfs(0, numbers[0]*(-1), 0)
    return answer[0]