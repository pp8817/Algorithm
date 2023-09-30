n, m = map(int, input().split())
board = list()
result = list()
for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        w = 0 #첫번째 블럭이 흰색인 경우
        b = 0 #첫번째 블럭이 검정색인 경우
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y)%2 == 0:
                    if board[x][y] == "W":
                        b+=1
                    else:
                        w+=1
                else:
                    if board[x][y] == "W":
                        w+=1
                    else:
                        b+=1
        result.append(w)
        result.append(b)
print(min(result))