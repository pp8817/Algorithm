from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    N = len(target)
    def check(word1, word2):
        cnt = 0
        for i in range(N):
            if word1[i] != word2[i]:
                cnt += 1
        
        return cnt == 1
    
    q = deque([(begin, 0)])
    
    while q:
        current_word, current_cnt = q.popleft()
        
        if current_word == target:
            return current_cnt
        
        for word in words:
            if check(current_word, word):
                words.remove(word)
                q.append((word, current_cnt+1))