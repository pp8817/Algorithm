import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import product

N, K = map(int, input().split())
K_list = list(map(str, input().split()))
length = len(str(N))

while True:
    temp = list(product(K_list, repeat=length))
    ex = []
    for i in temp:
        now = int("".join(i))
        if now <= N:
            ex.append(now)
    if ex:
        print(max(ex))
        break
    else:
        length -= 1