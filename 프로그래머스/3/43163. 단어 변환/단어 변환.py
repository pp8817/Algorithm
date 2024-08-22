from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    def promissing(word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1

        return count == 1
    
    q = deque([])
    q.append((begin, 0)) # 현재 단어, 변환 횟수
        
    while q:
        current_word, current_count = q.popleft()
        
        if current_word == target:
            return current_count
        
        for word in words:
            if promissing(current_word, word):
                q.append((word, current_count+1))
                words.remove(word)
              
    return 0