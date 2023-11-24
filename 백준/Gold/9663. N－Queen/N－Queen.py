def dfs(r):
    global cnt
    
    if r == N:
        cnt += 1
    else:
        for c in range(N):
            board[r] = c #퀸의 위치(행, 열) 지정
            
            #백트래킹
            if backtracking(r): # 퀸을 놓을 행에서 퀸의 위치 찾기 
                dfs(r+1)
                
            
def backtracking(r):
    for c in range(r): #현재 퀸을 놓으려는 행 이전의 행들을 체크
        if (board[r] == board[c]) or abs(board[r]-board[c]) == r-c: # 열이 같거나 대각선에 위치한다면
            return False
    return True


import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
board = [0] * N
cnt = 0
dfs(0)

print(cnt)