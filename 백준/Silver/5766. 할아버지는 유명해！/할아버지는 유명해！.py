import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    score = {}
    for _ in range(N):
        ranking = list(map(int, input().split()))
        for player in ranking:
            score[player] = score.get(player, 0) + 1
    
    max_score = max(score.values())

    second_score = 0
    for v in score.values():
        if v < max_score:
            second_score = max(v, second_score)
    
    result = [player for player, v in score.items() if v == second_score]
    result.sort()

    print(*result)