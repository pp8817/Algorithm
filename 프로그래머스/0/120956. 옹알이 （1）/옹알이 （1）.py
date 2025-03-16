from itertools import permutations

def solution(babbling):
    answer = 0
    words = ['aya', 'ye', 'woo', 'ma']
    # 최대 한 번씩 사용해 만들 수 있는 모든 조합의 수는 64개
    all_combinations = []
    for r in range(1, len(words) + 1):
        all_combinations.extend(permutations(words, r))
    
    result = [''.join(comb) for comb in all_combinations]
    
    for i in babbling:
        if i in result:
            answer += 1
    
    return answer