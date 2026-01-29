import sys
input = lambda: sys.stdin.readline().rstrip()

grid = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

def in_range(x, y):
    return 0 <= x < 19 and 0 <= y < 19

for x in range(19):
    for y in range(19):
        if grid[x][y] == 0:
            continue

        color = grid[x][y]

        for d in range(4):
            px = x - dx[d]
            py = y - dy[d]

            # 이전 칸이 같은 색이면 패스: 이미 처리된 정료
            if in_range(px, py) and grid[px][py] == color:
                continue

            cnt = 1
            nx, ny = x, y

            while True:
                nx += dx[d]
                ny += dy[d]

                if not in_range(nx, ny):
                    break
                if grid[nx][ny] != color:
                    break

                cnt += 1
            
            if cnt == 5:
                print(color)
                print(x+1, y+1)
                exit(0)

print(0)