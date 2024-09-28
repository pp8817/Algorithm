import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
target = int(input())

arr = [[0]*N for _ in range(N)]
arr[N//2][N//2]= 1

# 방향 벡터: 하,좌,상,우
dx = [1,0,-1,0]
dy = [0,-1,0,1] 

i = 2
start = 3
x,y = N//2, N//2

while x != 0 or y != 0:
    while i <= start*start: # target에 도달할 때까지
        if x == y == N//2:
            up,down,left,right = start,start-1,start-1,start-2
            x += dx[2]
            y += dy[2]
            up -= 1
            arr[x][y] = i
            i+=1


        while right > 0: # 우
            x += dx[-1]
            y += dy[-1]
            arr[x][y] = i
            right-=1
            i+=1

        while down > 0: # 하
            x += dx[0]
            y += dy[0]
            arr[x][y] = i
            down-=1
            i+=1

        while left > 0: # 좌
            x += dx[1]
            y += dy[1]
            arr[x][y] = i
            left-=1
            i+=1

        while up > 0: # 상
            x += dx[2]
            y += dy[2]
            arr[x][y] = i
            up-=1
            i+=1

    N -= 2
    start += 2

for j in range(len(arr)):
    print(*arr[j])
    if target in arr[j]:
        x = j+1
        y = arr[j].index(target) + 1
print(x,y)