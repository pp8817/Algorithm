import sys
input = sys.stdin.readline

n = int(input())
m = 1_000_000_007
dice = [list(map(int, input().split())) for _ in range(n)]

def mul(x, y, m): # 빠른 거듭제곱
    temp = 1
    while y > 0:
        if y % 2 != 0:
            temp *= x
            temp %= m
        x *= x
        x %= m
        y //= 2
    return temp

answer = 0
for b, a in dice:
    answer += (a * mul(b, m-2, m)) % m # 페르마의 소정리

print(answer % m)