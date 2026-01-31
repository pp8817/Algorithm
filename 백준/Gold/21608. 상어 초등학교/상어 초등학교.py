import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

grid = [[0]*N for _ in range(N)]
dic = {}
for _ in range(N**2):
    inp = list(map(int, input().split()))
    dic[inp[0]] = inp[1:]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for num, love in dic.items():
    stack = [] # [인접한 칸 중에 좋아하는 학생 수, 빈칸 수, 행, 열]
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0:
                continue
            
            temp = [0,0,-i,-j]
            for d in range(4):
                rx, ry = i+dx[d], j+dy[d]
                if 0<=rx<N and 0<=ry<N:
                    if grid[rx][ry] == 0:
                        temp[1] += 1
                        continue

                    elif grid[rx][ry] in love:
                        temp[0] += 1
                
            stack.append(temp)

    stack.sort()
    r, c = -1*stack[-1][2], -1*stack[-1][3]
    grid[r][c] = num

score = [0, 1, 10, 100, 1000]
ans = 0
for i in range(N):
    for j in range(N):
        num = grid[i][j]
        love = dic[num]
        cnt = 0
        for d in range(4):
            rx, ry = i+dx[d], j+dy[d]
            if 0<=rx<N and 0<=ry<N:
                if grid[rx][ry] in love:
                    cnt += 1
        
        ans += score[cnt]

print(ans)