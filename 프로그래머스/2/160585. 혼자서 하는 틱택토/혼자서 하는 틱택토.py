def solution(board): # 정상적인 게임 1, 아니면 0
    o_count = sum(row.count('O') for row in board)
    x_count = sum(row.count('X') for row in board)
    
    # 승리 조건 확인
    def check_winner(mark):
        # 가로, 세로, 대각선 확인
        return (
            any(all(cell == mark for cell in row) for row in board) or
            any(all(board[i][j] == mark for i in range(3)) for j in range(3)) or
            all(board[i][i] == mark for i in range(3)) or
            all(board[i][2-i] == mark for i in range(3))
        )

    o_wins = check_winner('O')
    x_wins = check_winner('X')

    if x_count > o_count:
        return 0

    if o_count > x_count + 1:
        return 0
    
    if o_wins and o_count != x_count + 1:
        return 0
    
    if x_wins and o_count != x_count:
        return 0
    
    if o_wins and x_wins:
        return 0
    
    return 1