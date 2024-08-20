import sys
input = lambda: sys.stdin.readline().rstrip()

# 먼지 확산
def spread():
    while dust:
        x,y,value = dust.pop()
        count = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=R or ny>=C:
                continue
            if (nx,ny) in cleaner:
                continue
            room[nx][ny]+=value//5
            count+=1
        room[x][y] -= (value//5)*count

# 공기청정기 가동
def clean(a,b):
    # 위에 회전
    x, y = a, 1
    index = 1 # 우부터 시작 우 상 좌 하
    temp = 0 # 공기청정기에서 나오는 바람
    while True:
        nx = x+dx[index]
        ny = y+dy[index]
        if nx==R or ny == C or nx==-1 or ny==-1: # 벽에 닿았을 때
            index = (index-1)%4
            continue
        if x==a and y==0: # 공기청정기로 다시 돌아옴
            break
        room[x][y], temp = temp, room[x][y] # swap
        x,y = nx, ny
    # 아래 회전
    x, y = b, 1
    index = 1 # 우부터 시작 우 하 좌 상
    temp = 0 # 공기청정기에서 나오는 바람
    while True:
        nx = x+dx[index]
        ny = y+dy[index]
        if nx==R or ny == C or nx==-1 or ny==-1: # 벽에 닿았을 때
            index = (index+1)%4
            continue
        if x==b and y==0: # 공기청정기로 다시 돌아옴
            break
        room[x][y], temp = temp, room[x][y] # swap
        x,y = nx, ny

R,C,T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
dust = []
cleaner = []

dx = [-1,0,1,0]
dy = [0,1,0,-1]          

for i,line in enumerate(room):
        for j, value in enumerate(line):
            if value>0:
                dust.append((i,j,value))
            if value==-1:
                cleaner.append((i,j))

a = cleaner[0][0] # 공기청정기의 윗부분
b = cleaner[1][0] # 공기청정기의 아랫부분
for t in range(T):
    spread()
    clean(a,b)
    for i,line in enumerate(room):
        for j, value in enumerate(line):
            if value>0:
                dust.append((i,j,value))
print(sum(dust[i][2] for i in range(len(dust))))
