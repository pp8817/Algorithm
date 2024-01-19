import sys
input = sys.stdin.readline

R,C,N = map(int, input().split()) # RxC공간, N초
grid = [[] for _ in range(R)]
d = [[1,0], [-1,0], [0,1], [0,-1]]
for i in range(R):
    str = input()
    for j in range(C):
        grid[i].append(str[j])
        

def dfs(grid):
    current_grid = [["O"]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if grid[i][j]=='O':
                current_grid[i][j] = '.'
                for x, y in d:
                    (dx, dy) = (x+i, y+j)
                    if 0<=dx<R and 0<=dy<C:
                        current_grid[dx][dy]='.'
    return current_grid
    
if N == 1:   # 초기 상태
    for i in range(R):
        print(''.join(grid[i]))
        
elif N % 2 == 0:   # 짝수 초에는 전체에 폭탄
    for i in range(R):
        print('O' * C)
        
elif N % 4 == 3:   # 초기 상태에서 폭탄 터진 상태
    result_grid = dfs(grid)
    for i in range(R):
        print(''.join(result_grid[i]))
elif N % 4 == 1:
    result_grid = dfs(grid)
    result_grid = dfs(result_grid)
    for i in range(R):
        print(''.join(result_grid[i]))