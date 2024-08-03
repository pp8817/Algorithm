import sys
input = lambda: sys.stdin().readline().rstrip()

def solution(board, h, w):
    count = 0
    
    H, W = len(board), len(board[0])
    
    color = board[h][w]
    d = [(0,1), (0,-1), (1,0), (-1,0)]
    
    for x, y in d:
        nx, ny = h+x, w+y
        if 0<=nx<H and 0<=ny<W:
            if board[nx][ny] == color:
                count+=1
    
    return count