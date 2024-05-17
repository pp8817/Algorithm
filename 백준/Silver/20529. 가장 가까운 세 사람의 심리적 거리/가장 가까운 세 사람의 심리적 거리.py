import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import combinations

T = int(input())

def mbti_dist(a, b):
    dist = 0
    for i, j in zip(a, b):
        if i != j:
            dist += 1
    return dist

for i in range(T):
    ans = 999999
    t = -1
    N = int(input())
    mbti = list(input().split())

    if N > 32:
        print(0)
    else:
        res = 99999
        case = combinations(mbti, 3)
        for a,b,c in case:
            dist = 0
            dist += mbti_dist(a, b)
            dist += mbti_dist(b, c)
            dist += mbti_dist(a, c)

            res = min(res, dist)
        print(res)

