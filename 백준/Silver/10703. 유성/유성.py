import sys
input = lambda: sys.stdin.readline().rstrip()

R, S = map(int, input().split())
maps = [list(input()) for _ in range(R)]
max_rows_nico = [-1]*S

for r in range(R):
    for c in range(S):
        if maps[r][c] == 'X':
            max_rows_nico[c] = r

D = R # 최대 거리로 초기화
for c in range(S):
    if max_rows_nico[c] != -1:
        temp_dist = 0
        for r in range(max_rows_nico[c] + 1, R):
            if maps[r][c] == '#':
                break
            temp_dist += 1
        D = min(D, temp_dist)

nicos = []
for r in range(R):
    for c in range(S):
        if maps[r][c] == 'X':
            nicos.append((r, c))
            maps[r][c] = '.'

for r, c in nicos:
    maps[r + D][c] = 'X'

# 4. 결과 출력 (join을 사용하여 속도 향상)
for row in maps:
    print("".join(row))