import sys
import copy
input = lambda: sys.stdin.readline().rstrip()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cctv_dirs = {
    1: [[0], [1], [2], [3]],
    2: [[0,2], [1,3]],
    3: [[0,1], [1,2], [2,3], [3,0]],
    4: [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
    5: [[0,1,2,3]]
}

def count_spot(board):
    count = 0
    for row in board:
        count += row.count(0)
    return count

def watch(board, x, y, dir):
    for d in dir:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if not (0 <= nx < N and 0 <= ny < M):
                break
            if board[nx][ny] == 6:
                break
            if board[nx][ny] == 0: 
                board[nx][ny] = '#'


def dfs(depth, board):
    global min_blind
    if depth == len(cctvs):
        min_blind = min(min_blind, count_spot(board))
        return

    x, y, cctv_type = cctvs[depth]
    for dirs in cctv_dirs[cctv_type]:
        copied = copy.deepcopy(board)
        watch(copied, x, y, dirs)
        dfs(depth + 1, copied)


N, M = map(int, input().split())
office = []
cctvs = []

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if 1 <= row[j] <= 5:
            cctvs.append((i, j, row[j]))
    office.append(row)

min_blind = N*M
dfs(0, office)

print(min_blind)