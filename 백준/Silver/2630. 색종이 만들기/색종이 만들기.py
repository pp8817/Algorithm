import sys
input = lambda: sys.stdin.readline().rstrip()

def solution(x, y, N) :
    global w, b
    color = paper[x][y]
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if color != paper[i][j] :
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    if color == 0 :
        w+=1
    else :
        b+=1

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)] 
w, b = 0,0

solution(0,0,N)
print(w)
print(b)
        
