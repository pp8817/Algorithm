answer = 0

def solution(word):
    alphabets = ["A","E","I","O","U"]
    
    def dfs(str):
        global answer
        answer += 1
        
        if str == word:
            return True
        if len(str) == 5:
            return False
        
        for alphabet in alphabets:
            if dfs(str+alphabet):
                return True
            
    for alphabet in alphabets:
        if dfs(alphabet):
            return answer