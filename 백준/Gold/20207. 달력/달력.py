import sys
input = lambda: sys.stdin.readline().rstrip()   

N = int(input())
days = [0]*366

for _ in range(N):
    S, E = map(int, input().split())
    
    for d in range(S, E+1):
        days[d] += 1

answer = 0
idx = 1

while idx <= 365:
    if days[idx] == 0:
        idx += 1
        continue
    
    width, hight = 0, 0

    while idx <= 365 and days[idx] > 0:
        width += 1
        hight = max(hight, days[idx])

        idx += 1
    
    answer += (width*hight)

print(answer)