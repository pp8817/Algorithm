import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
bulbs = list(map(int, input().split()))

for _ in range(M):
    a, b, c = map(int, input().split()) #a번째 명령어
    
    if a == 1:
        bulbs[b-1] = c
    elif a == 2:
        for idx in range(b-1, c):
            if bulbs[idx] == 1:
                bulbs[idx] = 0
            else:
                bulbs[idx] = 1
    elif a == 3:
        for idx in range(b-1, c):
            bulbs[idx] = 0
    else:
        for idx in range(b-1, c):
            bulbs[idx] = 1

print(*bulbs)