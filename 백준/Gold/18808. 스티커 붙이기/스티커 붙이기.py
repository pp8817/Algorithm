import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split()) # 세로, 가로, 스티커 개수

maps = [[0]*M for _ in range(N)]

# 회전 함수
def rotate_90(sticker):
    R = len(sticker) # 기존 행 개수
    C = len(sticker[0]) # 기존 열 개수
    rotated = [[0] * R for _ in range(C)]

    for i in range(R):
        for j in range(C):
            rotated[j][R - 1 - i] = sticker[i][j]
    return rotated

# 스티커 부착이 가능한지 검증하는 함수
def can_attach(x, y, sticker):
    R = len(sticker)
    C = len(sticker[0])
    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1 and maps[x+i][y+j] == 1:
                return False
    return True

# 스티커 붙이는 함수
def attach(x, y, sticker):
    R = len(sticker)
    C = len(sticker[0])
    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1:
                maps[x+i][y+j] = 1

def sol(sticker):
    for _ in range(4):  # 회전 시도
        R, C = len(sticker), len(sticker[0])
        for i in range(N - R + 1):  # 범위 내 행
            for j in range(M - C + 1):  # 범위 내 열
                if can_attach(i, j, sticker):
                    attach(i, j, sticker)
                    return
        # 회전
        sticker = rotate_90(sticker)

for _ in range(K):
    r, c = map(int, input().split()) # i번째 스티커의 행, 열
    sticker = []
    for _ in range(r):
        sticker.append(list(map(int, input().split())))

    sol(sticker)

result = 0
for i in range(N):
    result += sum(maps[i])

print(result)