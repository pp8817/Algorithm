import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, B = map(int, input().split())
grid = []
answer = int(1e9)
idx = 0

for i in range(N):
    grid.append(list(map(int, input().split())))

for f in range(257):
    exceed_block, lack_block = 0,0

    for i in range(N):
        for j in range(M):
            if grid[i][j]>f:
                exceed_block += grid[i][j] - f
            else:
                lack_block += f-grid[i][j]
    if exceed_block + B >= lack_block: #부족한 블럭보다 가진 블럭이 더 많다면 -> 평탄화 가능:
        if (exceed_block*2)+lack_block <= answer:
            answer = (exceed_block*2)+lack_block
            idx = f
print(answer, idx)