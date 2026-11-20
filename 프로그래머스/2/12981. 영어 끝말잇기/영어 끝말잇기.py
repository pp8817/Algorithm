# 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지
# n명이 끝말잇기를 할 때 탈락자의 [n번 사람, 몇 번째 단어] 출력

def solution(n, words):
    answer = []
    used = set() # 사용한 단어 중복 검사
    prev_word = None
    
    tmp = 1
    turn = 1
    
    for word in words:
        if (word in used) or (prev_word is not None) and (prev_word[-1] != word[0]):
            return [tmp, turn]
        
        used.add(word)
        prev_word = word
        
        if tmp == n: # 마지막 사람 순서가 끝났다면 턴 +1
            turn += 1
            tmp = 1
        else:
            tmp += 1
        

    return [0,0]