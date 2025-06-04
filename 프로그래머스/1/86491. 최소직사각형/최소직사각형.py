# 각 명함을 돌리면서 명함을 돌려도 기존 길이 최댓값보다 작다면 통과
def solution(sizes):
    rotated = [sorted(card, reverse=True) for card in sizes]
    return max(card[0] for card in rotated) * max(card[1] for card in rotated)